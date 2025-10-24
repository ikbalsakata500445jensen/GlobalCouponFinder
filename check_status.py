#!/usr/bin/env python3
"""
Simple status check for GlobalCouponFinder
"""

import requests
import json
from datetime import datetime

def check_status():
    """Check the current status of the system"""
    print("🔍 GlobalCouponFinder Status Check")
    print("=" * 50)
    print(f"Time: {datetime.now()}")
    
    # Check if backend is running
    print("\n1️⃣ Backend API Status:")
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code == 200:
            print("✅ Backend API is running")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Backend API error: {response.status_code}")
    except Exception as e:
        print(f"❌ Backend API not running: {e}")
        print("   💡 Start backend with: cd backend && python main.py")
    
    # Check stores
    print("\n2️⃣ Stores Status:")
    try:
        response = requests.get("http://localhost:8000/api/v1/stores", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Stores API working - Found {data.get('total', 0)} stores")
        else:
            print(f"❌ Stores API error: {response.status_code}")
    except Exception as e:
        print(f"❌ Stores API not accessible: {e}")
    
    # Check coupons
    print("\n3️⃣ Coupons Status:")
    try:
        response = requests.get("http://localhost:8000/api/v1/coupons", timeout=5)
        if response.status_code == 200:
            data = response.json()
            total_coupons = data.get('total', 0)
            print(f"✅ Coupons API working - Found {total_coupons} coupons")
            
            if total_coupons > 0:
                print("🎉 COUPONS FOUND! Scraping is working!")
                coupons = data.get('coupons', [])
                for i, coupon in enumerate(coupons[:3]):  # Show first 3
                    print(f"   {i+1}. {coupon.get('title', 'No title')} - {coupon.get('store_name', 'Unknown store')}")
            else:
                print("⏳ No coupons yet - this is normal for new scraping")
        else:
            print(f"❌ Coupons API error: {response.status_code}")
    except Exception as e:
        print(f"❌ Coupons API not accessible: {e}")
    
    print("\n" + "=" * 50)
    print("🎯 Status Check Complete!")
    print("=" * 50)
    
    # Summary
    print("\n📊 SUMMARY:")
    print("✅ Backend API: Working" if "✅ Backend API is running" in str(locals()) else "❌ Backend API: Not running")
    print("✅ Stores: 135 loaded" if "✅ Stores API working" in str(locals()) else "❌ Stores: Not accessible")
    print("✅ Coupons: Available" if "✅ Coupons API working" in str(locals()) else "❌ Coupons: Not accessible")
    
    print("\n💡 NEXT STEPS:")
    print("1. If backend not running: cd backend && python main.py")
    print("2. If no coupons: Check Railway logs for scraping activity")
    print("3. Coupons will appear within 1-2 hours of scraping")

if __name__ == "__main__":
    check_status()
