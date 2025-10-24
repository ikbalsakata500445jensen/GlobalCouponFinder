#!/usr/bin/env python3
"""
Test script to check if Railway scraping service is working
"""

import requests
import json
import time
from datetime import datetime

def test_railway_service():
    """Test if Railway scraping service is working"""
    print("🔍 Testing Railway Scraping Service")
    print("=" * 50)
    
    # Test 1: Check if backend API is running
    print("1️⃣ Testing Backend API...")
    try:
        response = requests.get("http://localhost:8000/health", timeout=10)
        if response.status_code == 200:
            print("✅ Backend API is running")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Backend API error: {response.status_code}")
    except Exception as e:
        print(f"❌ Backend API not accessible: {e}")
    
    # Test 2: Check stores endpoint
    print("\n2️⃣ Testing Stores API...")
    try:
        response = requests.get("http://localhost:8000/api/v1/stores", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Stores API working - Found {data.get('total', 0)} stores")
        else:
            print(f"❌ Stores API error: {response.status_code}")
    except Exception as e:
        print(f"❌ Stores API not accessible: {e}")
    
    # Test 3: Check region stats
    print("\n3️⃣ Testing Region Stats...")
    try:
        response = requests.get("http://localhost:8000/api/v1/stores/regions/stats", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print("✅ Region stats working:")
            for region, stats in data.get('stats', {}).items():
                print(f"   {region}: {stats.get('stores', 0)} stores, {stats.get('coupons', 0)} coupons")
        else:
            print(f"❌ Region stats error: {response.status_code}")
    except Exception as e:
        print(f"❌ Region stats not accessible: {e}")
    
    # Test 4: Check if coupons exist
    print("\n4️⃣ Testing Coupons...")
    try:
        response = requests.get("http://localhost:8000/api/v1/coupons", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Coupons API working - Found {data.get('total', 0)} coupons")
        else:
            print(f"❌ Coupons API error: {response.status_code}")
    except Exception as e:
        print(f"❌ Coupons API not accessible: {e}")
    
    print("\n" + "=" * 50)
    print("🎯 Railway Service Test Complete!")
    print("=" * 50)

def test_railway_logs():
    """Instructions for checking Railway logs"""
    print("\n📋 How to Check Railway Logs:")
    print("1. Go to your Railway dashboard")
    print("2. Click on your service")
    print("3. Go to 'Logs' tab")
    print("4. Look for these messages:")
    print("   ✅ 'Starting Celery Worker...'")
    print("   ✅ 'Starting Celery Beat...'")
    print("   ✅ 'Scraped [Store Name]: X new, Y updated'")
    print("   ❌ Any error messages in red")

def test_railway_environment():
    """Check Railway environment variables"""
    print("\n🔧 Railway Environment Variables Check:")
    print("Make sure these are set in Railway:")
    print("✅ DATABASE_URL")
    print("✅ REDIS_URL") 
    print("✅ PLAYWRIGHT_BROWSERS_PATH")
    print("✅ HEADLESS")
    print("✅ SCRAPE_FREQUENCY_MINUTES")
    print("✅ USE_PROXIES")
    print("✅ SERVICE_TYPE (worker or beat)")

if __name__ == "__main__":
    test_railway_service()
    test_railway_logs()
    test_railway_environment()
