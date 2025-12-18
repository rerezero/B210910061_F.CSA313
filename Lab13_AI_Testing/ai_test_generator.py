"""
Лаборатори 13: AI-Powered Automated Testing
Claude API ашиглан автомат тест үүсгэх
"""

import json
from typing import Optional

# Note: In production, use: pip install anthropic
# from anthropic import Anthropic


class AITestGenerator:
    """AI ашиглан тест үүсгэх класс"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize AI Test Generator
        
        Args:
            api_key: Anthropic API key (optional for demo)
        """
        self.api_key = api_key
        self.model = "claude-sonnet-4-20250514"
    
    def generate_unit_tests(self, source_code: str, language: str = "Java") -> str:
        """
        Код шинжилж unit тест үүсгэх
        
        Args:
            source_code: Тестлэх код
            language: Програмчлалын хэл
            
        Returns:
            Үүсгэсэн тестийн код
        """
        prompt = f"""Analyze the following {language} code and generate 
comprehensive unit tests. Include:
1. Normal cases
2. Edge cases  
3. Error cases
4. Boundary value tests

Source code:
```{language.lower()}
{source_code}
```

Generate JUnit 5 tests with @Test annotations and assertions."""

        # Demo response (actual API call would go here)
        return self._demo_response("unit_tests", source_code)
    
    def analyze_code_for_bugs(self, source_code: str) -> str:
        """
        Код дахь боломжит алдаануудыг илрүүлэх
        
        Args:
            source_code: Шинжлэх код
            
        Returns:
            Алдааны тайлан
        """
        prompt = f"""Analyze this code for potential bugs:
```
{source_code}
```

List all potential issues:
1. Logic errors
2. Null pointer risks
3. Off-by-one errors
4. Resource leaks

Format: [SEVERITY] Description - Line number"""

        return self._demo_response("bug_analysis", source_code)
    
    def generate_test_data(self, schema: dict, count: int = 10) -> str:
        """
        Тест өгөгдөл үүсгэх
        
        Args:
            schema: Өгөгдлийн бүтэц
            count: Үүсгэх тоо
            
        Returns:
            JSON тест өгөгдөл
        """
        prompt = f"""Generate {count} test data records for this schema:
{json.dumps(schema, indent=2)}

Include valid data, edge cases, and invalid data for negative testing.
Output as JSON array."""

        return self._demo_response("test_data", json.dumps(schema))
    
    def _demo_response(self, response_type: str, context: str) -> str:
        """Demo responses for testing without API"""
        
        if response_type == "unit_tests":
            return '''
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {
    private Calculator calc = new Calculator();
    
    @Test
    void testNormalDivision() {
        assertEquals(5, calc.divide(10, 2));
    }
    
    @Test
    void testDivisionByZero() {
        assertThrows(ArithmeticException.class, () -> {
            calc.divide(10, 0);
        });
    }
    
    @Test
    void testNegativeDivision() {
        assertEquals(-5, calc.divide(-10, 2));
        assertEquals(-5, calc.divide(10, -2));
        assertEquals(5, calc.divide(-10, -2));
    }
    
    @Test
    void testDivisionResultZero() {
        assertEquals(0, calc.divide(0, 5));
    }
    
    @Test
    void testLargeNumbers() {
        assertEquals(1000000, calc.divide(1000000000, 1000));
    }
}
'''
        
        elif response_type == "bug_analysis":
            return '''
[HIGH] Division by zero not handled - Line 3
  Risk: ArithmeticException when b=0
  Fix: Add validation: if (b == 0) throw new IllegalArgumentException()

[MEDIUM] No input validation - Line 2
  Risk: Unexpected behavior with extreme values
  Fix: Add bounds checking for parameters

[LOW] Integer overflow possible - Line 3
  Risk: When a is Integer.MIN_VALUE and b is -1
  Fix: Use long or check bounds before operation
'''
        
        elif response_type == "test_data":
            return json.dumps([
                {"name": "John Doe", "age": 25, "email": "john@test.com", "balance": 1500.50},
                {"name": "", "age": 18, "email": "edge@test.com", "balance": 0.00},
                {"name": "A", "age": 100, "email": "max@test.com", "balance": 999999.99},
                {"name": "Invalid", "age": 17, "email": "invalid-email", "balance": -100},
                {"name": "Тест User", "age": 50, "email": "test@example.com", "balance": 500.00}
            ], indent=2, ensure_ascii=False)
        
        return "Unknown response type"


# ============ DEMO USAGE ============

def demo():
    """AI Test Generator демо"""
    
    print("=" * 60)
    print("Lab 13: AI-Powered Automated Testing")
    print("=" * 60)
    
    generator = AITestGenerator()
    
    # Demo 1: Generate Unit Tests
    print("\n1. UNIT TEST GENERATION")
    print("-" * 40)
    
    java_code = """
public class Calculator {
    public int divide(int a, int b) {
        return a / b;
    }
}
"""
    
    print("Input code:")
    print(java_code)
    print("\nGenerated tests:")
    print(generator.generate_unit_tests(java_code))
    
    # Demo 2: Bug Analysis
    print("\n2. BUG ANALYSIS")
    print("-" * 40)
    
    print("Analysis result:")
    print(generator.analyze_code_for_bugs(java_code))
    
    # Demo 3: Test Data Generation
    print("\n3. TEST DATA GENERATION")
    print("-" * 40)
    
    schema = {
        "user": {
            "name": "string",
            "age": "integer (18-100)",
            "email": "email format",
            "balance": "decimal"
        }
    }
    
    print("Schema:")
    print(json.dumps(schema, indent=2))
    print("\nGenerated test data:")
    print(generator.generate_test_data(schema, count=5))
    
    print("\n" + "=" * 60)
    print("AI Testing Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    demo()
