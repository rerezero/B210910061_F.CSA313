# Чанарын Баталгаа ба Туршилт

├── Lab01_Selenium/          # Selenium WebDriver automation
├── Lab02_JMeter/            # Performance testing with JMeter
├── Lab03_Postman/           # API testing with Postman/Newman
├── Lab04_MockServer/        # Dynamic mock server (Express.js)
├── Lab05_SystemTesting/     # System testing - Airport Connection
├── Lab07_ExploratoryTesting/# Exploratory testing session
├── Lab08_UnitTesting/       # Unit testing - Meeting Planner (JUnit 5)
├── Lab09_StructuralTesting/ # Code coverage (JaCoCo)
├── Lab10_DataflowTesting/   # Definition-Use pairs analysis
├── Lab11_MutationTesting/   # Mutation testing (PITest)
├── Lab12_FSM_Elevator/      # Finite State Machine testing
├── Lab13_AI_Testing/        # AI-powered automated testing
└── README.md



| Lab | Title | Technology | Status |
|-----|-------|------------|--------|
| 01 | Selenium WebDriver | Python, Selenium | ✅ Complete |
| 02 | JMeter Performance | Apache JMeter | ✅ Complete |
| 03 | Postman API Testing | Postman, Newman | ✅ Complete |
| 04 | Mock Server | Node.js, Express | ✅ Complete |
| 05 | System Testing | Choice-based | ✅ Complete |
| 07 | Exploratory Testing | Session-based | ✅ Complete |
| 08 | Unit Testing | JUnit 5, Maven | ✅ Complete |
| 09 | Structural Testing | JaCoCo | ✅ Complete |
| 10 | Dataflow Testing | DU-Pairs | ✅ Complete |
| 11 | Mutation Testing | PITest | ✅ Complete |
| 12 | FSM Testing | State Machines | ✅ Complete |
| 13 | AI Testing | Claude API | ✅ Complete |



### Lab 01: Selenium
```bash
cd Lab01_Selenium
pip install -r requirements.txt
pytest test_login.py -v
```

### Lab 02: JMeter
```bash
cd Lab02_JMeter
jmeter -n -t binance_test.jmx -l results.jtl
```

### Lab 03: Postman
```bash
cd Lab03_Postman
newman run binance-collection.json
```

### Lab 04: Mock Server
```bash
cd Lab04_MockServer
npm install
npm start
```

### Lab 05: System Testing
```bash
cd Lab05_SystemTesting
python test_airport_connection.py
```

### Lab 08: Unit Testing
```bash
cd Lab08_UnitTesting
mvn clean test
mvn jacoco:report  # Coverage report
```

### Lab 12: FSM Testing
```bash
cd Lab12_FSM_Elevator
python elevator_fsm.py
```

### Lab 13: AI Testing
```bash
cd Lab13_AI_Testing
python ai_test_generator.py
```

---

##  Technologies

| Category | Tools |
|----------|-------|
| Languages | Java, Python, JavaScript |
| Testing Frameworks | JUnit 5, pytest, Selenium |
| Coverage | JaCoCo |
| Mutation | PITest |
| Performance | JMeter |
| API Testing | Postman, Newman |
| Backend | Node.js, Express |
| AI | Claude API |

---

## Key Results

### Lab 08: Unit Testing
- **5 bugs found** in Meeting Planner
- **30+ test cases** written
- **93% code coverage**

### Lab 11: Mutation Testing
- **82% mutation score**
- 31/38 mutants killed

### Lab 05: System Testing
- **12 test cases** from choice-based analysis
- All boundary conditions covered

