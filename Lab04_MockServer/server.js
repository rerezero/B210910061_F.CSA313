/**
 * Лаборатори 04: Dynamic Mock Server
 * Express.js ашиглан API mock server үүсгэх
 */

const express = require('express');
const app = express();
app.use(express.json());

// ============ IN-MEMORY DATA STORE ============
let users = [
    { id: 1, name: "Бат", email: "bat@example.com", balance: 50000 },
    { id: 2, name: "Болд", email: "bold@example.com", balance: 75000 },
    { id: 3, name: "Сараа", email: "saraa@example.com", balance: 100000 }
];

let transactions = [];
let requestCount = 0;
let simulateError = false;
let simulateDelay = 0;

// ============ MIDDLEWARE ============

// Request counter & logger
app.use((req, res, next) => {
    requestCount++;
    console.log(`[${new Date().toISOString()}] #${requestCount} ${req.method} ${req.path}`);
    next();
});

// Delay simulation
app.use((req, res, next) => {
    if (simulateDelay > 0) {
        setTimeout(next, simulateDelay);
    } else {
        next();
    }
});

// Error simulation
app.use((req, res, next) => {
    if (simulateError && !req.path.startsWith('/admin')) {
        return res.status(500).json({ 
            error: "Internal Server Error",
            message: "Simulated error for testing"
        });
    }
    next();
});

// ============ USER ENDPOINTS ============

// GET /users - Бүх хэрэглэгчдийг авах
app.get('/users', (req, res) => {
    const { limit, offset } = req.query;
    let result = [...users];
    
    if (offset) result = result.slice(parseInt(offset));
    if (limit) result = result.slice(0, parseInt(limit));
    
    res.json({
        success: true,
        count: result.length,
        total: users.length,
        data: result
    });
});

// GET /users/:id - Нэг хэрэглэгч авах
app.get('/users/:id', (req, res) => {
    const user = users.find(u => u.id === parseInt(req.params.id));
    
    if (!user) {
        return res.status(404).json({ 
            success: false, 
            error: "User not found",
            id: req.params.id
        });
    }
    
    res.json({ success: true, data: user });
});

// POST /users - Шинэ хэрэглэгч үүсгэх
app.post('/users', (req, res) => {
    const { name, email, balance } = req.body;
    
    // Validation
    if (!name || !email) {
        return res.status(400).json({
            success: false,
            error: "Validation failed",
            details: {
                name: !name ? "Name is required" : null,
                email: !email ? "Email is required" : null
            }
        });
    }
    
    // Email format validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        return res.status(400).json({
            success: false,
            error: "Invalid email format"
        });
    }
    
    // Check duplicate email
    if (users.find(u => u.email === email)) {
        return res.status(409).json({
            success: false,
            error: "Email already exists"
        });
    }
    
    const newUser = {
        id: Math.max(...users.map(u => u.id)) + 1,
        name,
        email,
        balance: balance || 0,
        createdAt: new Date().toISOString()
    };
    
    users.push(newUser);
    
    res.status(201).json({ 
        success: true, 
        message: "User created successfully",
        data: newUser 
    });
});

// PUT /users/:id - Хэрэглэгч засах
app.put('/users/:id', (req, res) => {
    const index = users.findIndex(u => u.id === parseInt(req.params.id));
    
    if (index === -1) {
        return res.status(404).json({ 
            success: false,
            error: "User not found" 
        });
    }
    
    const { name, email, balance } = req.body;
    
    // Check email uniqueness if changing
    if (email && email !== users[index].email) {
        if (users.find(u => u.email === email)) {
            return res.status(409).json({
                success: false,
                error: "Email already exists"
            });
        }
    }
    
    users[index] = { 
        ...users[index], 
        ...req.body,
        updatedAt: new Date().toISOString()
    };
    
    res.json({ 
        success: true, 
        message: "User updated successfully",
        data: users[index] 
    });
});

// DELETE /users/:id - Хэрэглэгч устгах
app.delete('/users/:id', (req, res) => {
    const index = users.findIndex(u => u.id === parseInt(req.params.id));
    
    if (index === -1) {
        return res.status(404).json({ 
            success: false,
            error: "User not found" 
        });
    }
    
    const deleted = users.splice(index, 1)[0];
    
    res.json({ 
        success: true, 
        message: "User deleted successfully",
        data: deleted 
    });
});

// ============ TRANSACTION ENDPOINTS ============

// POST /transfer - Мөнгө шилжүүлэх
app.post('/transfer', (req, res) => {
    const { fromId, toId, amount, description } = req.body;
    
    // Validation
    if (!fromId || !toId || !amount) {
        return res.status(400).json({ 
            success: false,
            error: "Missing required fields: fromId, toId, amount" 
        });
    }
    
    if (amount <= 0) {
        return res.status(400).json({ 
            success: false,
            error: "Amount must be positive" 
        });
    }
    
    if (fromId === toId) {
        return res.status(400).json({ 
            success: false,
            error: "Cannot transfer to same account" 
        });
    }
    
    const fromUser = users.find(u => u.id === fromId);
    const toUser = users.find(u => u.id === toId);
    
    if (!fromUser) {
        return res.status(404).json({ 
            success: false,
            error: "Sender not found" 
        });
    }
    
    if (!toUser) {
        return res.status(404).json({ 
            success: false,
            error: "Recipient not found" 
        });
    }
    
    if (fromUser.balance < amount) {
        return res.status(400).json({ 
            success: false,
            error: "Insufficient balance",
            available: fromUser.balance,
            requested: amount
        });
    }
    
    // Perform transfer
    fromUser.balance -= amount;
    toUser.balance += amount;
    
    const transaction = {
        id: transactions.length + 1,
        fromId,
        toId,
        amount,
        description: description || "Transfer",
        timestamp: new Date().toISOString()
    };
    
    transactions.push(transaction);
    
    res.json({
        success: true,
        message: `Transferred ${amount} from ${fromUser.name} to ${toUser.name}`,
        transaction,
        balances: {
            sender: { id: fromId, balance: fromUser.balance },
            recipient: { id: toId, balance: toUser.balance }
        }
    });
});

// GET /transactions - Гүйлгээний түүх
app.get('/transactions', (req, res) => {
    const { userId, limit } = req.query;
    
    let result = [...transactions];
    
    if (userId) {
        const id = parseInt(userId);
        result = result.filter(t => t.fromId === id || t.toId === id);
    }
    
    if (limit) {
        result = result.slice(-parseInt(limit));
    }
    
    res.json({
        success: true,
        count: result.length,
        data: result
    });
});

// ============ ADMIN ENDPOINTS ============

// POST /admin/reset - Серверийг reset хийх
app.post('/admin/reset', (req, res) => {
    users = [
        { id: 1, name: "Бат", email: "bat@example.com", balance: 50000 },
        { id: 2, name: "Болд", email: "bold@example.com", balance: 75000 },
        { id: 3, name: "Сараа", email: "saraa@example.com", balance: 100000 }
    ];
    transactions = [];
    requestCount = 0;
    simulateError = false;
    simulateDelay = 0;
    
    res.json({ 
        success: true,
        message: "Server reset complete" 
    });
});

// POST /admin/simulate-error - Алдаа симуляц
app.post('/admin/simulate-error', (req, res) => {
    simulateError = req.body.enable === true;
    res.json({ 
        success: true,
        simulateError 
    });
});

// POST /admin/simulate-delay - Delay симуляц
app.post('/admin/simulate-delay', (req, res) => {
    simulateDelay = parseInt(req.body.ms) || 0;
    res.json({ 
        success: true,
        simulateDelay: `${simulateDelay}ms`
    });
});

// GET /admin/stats - Статистик
app.get('/admin/stats', (req, res) => {
    res.json({
        success: true,
        stats: {
            totalRequests: requestCount,
            totalUsers: users.length,
            totalTransactions: transactions.length,
            totalBalance: users.reduce((sum, u) => sum + u.balance, 0),
            simulateError,
            simulateDelay
        }
    });
});

// GET /health - Health check
app.get('/health', (req, res) => {
    res.json({ 
        status: "healthy",
        timestamp: new Date().toISOString(),
        uptime: process.uptime()
    });
});

// ============ START SERVER ============
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`
╔════════════════════════════════════════════╗
║     Mock Server Running on Port ${PORT}        ║
║                                            ║
║  Endpoints:                                ║
║  - GET    /users                           ║
║  - GET    /users/:id                       ║
║  - POST   /users                           ║
║  - PUT    /users/:id                       ║
║  - DELETE /users/:id                       ║
║  - POST   /transfer                        ║
║  - GET    /transactions                    ║
║  - GET    /health                          ║
║  - POST   /admin/reset                     ║
║  - POST   /admin/simulate-error            ║
║  - POST   /admin/simulate-delay            ║
║  - GET    /admin/stats                     ║
╚════════════════════════════════════════════╝
    `);
});

module.exports = app;
