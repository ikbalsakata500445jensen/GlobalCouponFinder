#!/usr/bin/env python3
"""
Test script to check coupons and scraping activity
"""

import requests
import json
import time
from datetime import datetime

def test_coupons():
    """Test coupons API and check for scraping activity"""
    print("🔍 Testing Coupons and Scraping Activity")
    print("=" * 50)
    
    base_url = "http://localhost:8000"
    
    # Test 1: Check coupons endpoint
    print("1️⃣ Testing Coupons Endpoint...")
    try:
        response = requests.get(f"{base_url}/api/v1/coupons", timeout=5)
        if response.status_code == 200:
            data = response.json()
            total_coupons = data.get('total', 0)
            print(f"✅ Coupons endpoint working - Found {total_coupons} coupons")
            
            if total_coupons > 0:
                print("🎉 COUPONS FOUND! Scraping is working!")
                coupons = data.get('coupons', [])
                for i, coupon in enumerate(coupons[:5]):  # Show first 5
                    print(f"   {i+1}. {coupon.get('title', 'No title')} - {coupon.get('store_name', 'Unknown store')}")
            else:
                print("⏳ No coupons yet - this is normal for new scraping")
        else:
            print(f"❌ Coupons endpoint error: {response.status_code}")
    except Exception as e:
        print(f"❌ Coupons endpoint not accessible: {e}")
    
    # Test 2: Check specific store coupons
    print("\n2️⃣ Testing Store-Specific Coupons...")
    try:
        # Test a few popular stores
        test_stores = ["amazon-us", "walmart", "target"]
        for store_slug in test_stores:
            response = requests.get(f"{base_url}/api/v1/coupons?store_slug={store_slug}", timeout=5)
            if response.status_code == 200:
                data = response.json()
                count = data.get('total', 0)
                print(f"   {store_slug}: {count} coupons")
            else:
                print(f"   {store_slug}: Error {response.status_code}")
    except Exception as e:
        print(f"❌ Store-specific coupons error: {e}")
    
    # Test 3: Check region-specific coupons
    print("\n3️⃣ Testing Region-Specific Coupons...")
    try:
        regions = ["america", "europe", "asia"]
        for region in regions:
            response = requests.get(f"{base_url}/api/v1/coupons?region={region}", timeout=5)
            if response.status_code == 200:
                data = response.json()
                count = data.get('total', 0)
                print(f"   {region}: {count} coupons")
            else:
                print(f"   {region}: Error {response.status_code}")
    except Exception as e:
        print(f"❌ Region-specific coupons error: {e}")
    
    # Test 4: Check food delivery coupons
    print("\n4️⃣ Testing Food Delivery Coupons...")
    try:
        response = requests.get(f"{base_url}/api/v1/coupons?store_type=food_delivery", timeout=5)
        if response.status_code == 200:
            data = response.json()
            count = data.get('total', 0)
            print(f"   Food delivery: {count} coupons")
        else:
            print(f"   Food delivery: Error {response.status_code}")
    except Exception as e:
        print(f"❌ Food delivery coupons error: {e}")
    
    print("\n" + "=" * 50)
    print("🎯 Coupon Test Complete!")
    print("=" * 50)
    
    # Summary
    if total_coupons > 0:
        print("🎉 SUCCESS! Your scraping is working and collecting coupons!")
    else:
        print("⏳ No coupons yet - this is normal. Scraping takes time.")
        print("💡 Check Railway logs for scraping activity")
        print("💡 Coupons will appear within 1-2 hours")

if __name__ == "__main__":
    test_coupons()
