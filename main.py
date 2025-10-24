#!/usr/bin/env python3
"""
GlobalCouponFinder - Main Entry Point
This file helps Railway detect this as a Python project.
The actual scraping service runs from the scrapers/ directory.
"""

import os
import sys
import subprocess
import time

def main():
    """Main entry point for Railway deployment"""
    print("🚀 GlobalCouponFinder Scraping Service")
    print("=" * 50)
    print(f"Python version: {sys.version}")
    print(f"Working directory: {os.getcwd()}")
    print(f"Environment: {os.getenv('RAILWAY_ENVIRONMENT', 'Not Railway')}")
    
    # Check if scrapers directory exists
    if not os.path.exists('scrapers'):
        print("❌ scrapers directory not found!")
        print("Available files:", os.listdir('.'))
        sys.exit(1)
    
    # Change to scrapers directory
    print("📁 Changing to scrapers directory...")
    os.chdir('scrapers')
    print(f"New working directory: {os.getcwd()}")
    
    # Check if celery_app.py exists
    if not os.path.exists('celery_app.py'):
        print("❌ celery_app.py not found in scrapers directory!")
        print("Available files:", os.listdir('.'))
        sys.exit(1)
    
    # Determine which service to run based on environment
    service_type = os.getenv('SERVICE_TYPE', 'worker')
    print(f"🔧 Service type: {service_type}")
    
    try:
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
    except KeyboardInterrupt:
        print("🛑 Shutting down gracefully...")
    except Exception as e:
        print(f"❌ Error starting service: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
