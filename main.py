#!/usr/bin/env python3
"""
GlobalCouponFinder - Main Entry Point
This file helps Railway detect this as a Python project.
The actual scraping service runs from the scrapers/ directory.
"""

import os
import sys
import subprocess

def main():
    """Main entry point for Railway deployment"""
    print("🚀 GlobalCouponFinder Scraping Service")
    print("=" * 50)
    
    # Check if we're in Railway environment
    if os.getenv('RAILWAY_ENVIRONMENT'):
        print("✅ Running on Railway")
        
        # Change to scrapers directory
        os.chdir('scrapers')
        
        # Determine which service to run based on environment
        service_type = os.getenv('SERVICE_TYPE', 'worker')
        
        if service_type == 'beat':
            print("🕐 Starting Celery Beat Scheduler...")
            subprocess.run([
                'celery', '-A', 'celery_app', 'beat', '--loglevel=info'
            ])
        else:
            print("👷 Starting Celery Worker...")
            subprocess.run([
                'celery', '-A', 'celery_app', 'worker', 
                '--loglevel=info', '--concurrency=5'
            ])
    else:
        print("❌ Not running on Railway")
        print("This service is designed to run on Railway.app")
        sys.exit(1)

if __name__ == "__main__":
    main()
