"""
Simple script to run the test suite and verify all functionality.
"""

import sys
import subprocess


def run_tests():
    """Run the test suite and display results."""
    print("=" * 60)
    print("RUNNING COMPREHENSIVE TEST SUITE")
    print("=" * 60)
    
    try:
        # Run the test file
        result = subprocess.run([sys.executable, "test_task1.py"], 
                              capture_output=True, text=True, timeout=30)
        
        print("STDOUT:")
        print(result.stdout)
        
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
        
        print(f"Return code: {result.returncode}")
        
        if result.returncode == 0:
            print("✓ All tests passed successfully!")
        else:
            print("✗ Some tests failed!")
            
    except subprocess.TimeoutExpired:
        print("✗ Tests timed out!")
    except Exception as e:
        print(f"✗ Error running tests: {e}")


def run_demo():
    """Run the demo to show functionality."""
    print("\n" + "=" * 60)
    print("RUNNING DEMO")
    print("=" * 60)
    
    try:
        result = subprocess.run([sys.executable, "demo.py"], 
                              capture_output=True, text=True, timeout=30)
        
        print("DEMO OUTPUT:")
        print(result.stdout)
        
        if result.stderr:
            print("DEMO ERRORS:")
            print(result.stderr)
            
    except subprocess.TimeoutExpired:
        print("✗ Demo timed out!")
    except Exception as e:
        print(f"✗ Error running demo: {e}")


if __name__ == "__main__":
    # Run tests
    run_tests()
    
    # Run demo
    run_demo()
    
    print("\n" + "=" * 60)
    print("TESTING COMPLETE")
    print("=" * 60)
    print("To run the interactive program, execute: python task1.py")
    print("To run the demo, execute: python demo.py")
    print("To run tests, execute: python test_task1.py")
