#!/usr/bin/env python3
"""
Test script to check if backend API is working locally
"""

import requests
import json
import time
from datetime import datetime

def test_backend():
    """Test backend API locally"""
    print("🔍 Testing Backend API Locally")
    print("=" * 50)
    
    base_url = "http://localhost:8000"
    
    # Test 1: Health check
    print("1️⃣ Testing Health Endpoint...")
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            print("✅ Health endpoint working")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health endpoint error: {response.status_code}")
    except Exception as e:
        print(f"❌ Health endpoint not accessible: {e}")
        print("   Make sure to run: cd backend && uvicorn main:app --reload")
    
    # Test 2: Root endpoint
    print("\n2️⃣ Testing Root Endpoint...")
    try:
        response = requests.get(f"{base_url}/", timeout=5)
        if response.status_code == 200:
            print("✅ Root endpoint working")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Root endpoint error: {response.status_code}")
    except Exception as e:
        print(f"❌ Root endpoint not accessible: {e}")
    
    # Test 3: Stores endpoint
    print("\n3️⃣ Testing Stores Endpoint...")
    try:
        response = requests.get(f"{base_url}/api/v1/stores", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Stores endpoint working - Found {data.get('total', 0)} stores")
        else:
            print(f"❌ Stores endpoint error: {response.status_code}")
    except Exception as e:
        print(f"❌ Stores endpoint not accessible: {e}")
    
    # Test 4: Region stats
    print("\n4️⃣ Testing Region Stats...")
    try:
        response = requests.get(f"{base_url}/api/v1/stores/regions/stats", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print("✅ Region stats working:")
            for region, stats in data.get('stats', {}).items():
                print(f"   {region}: {stats.get('stores', 0)} stores, {stats.get('coupons', 0)} coupons")
        else:
            print(f"❌ Region stats error: {response.status_code}")
    except Exception as e:
        print(f"❌ Region stats not accessible: {e}")
    
    print("\n" + "=" * 50)
    print("🎯 Backend Test Complete!")
    print("=" * 50)

if __name__ == "__main__":
    test_backend()
