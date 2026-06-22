# test_ledgerfuel.py
"""
Tests for LedgerFuel module.
"""

import unittest
from ledgerfuel import LedgerFuel

class TestLedgerFuel(unittest.TestCase):
    """Test cases for LedgerFuel class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LedgerFuel()
        self.assertIsInstance(instance, LedgerFuel)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LedgerFuel()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
