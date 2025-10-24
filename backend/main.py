from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
from datetime import datetime

# Import routers (to be created)
# from routers import coupons, users, auth, subscriptions

app = FastAPI(
    title="GlobalCouponFinder API",
    description="API for scraping and managing global coupon codes",
    version="1.0.0"
)

# CORS configuration
origins = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to GlobalCouponFinder API",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat(),
        "status": "operational"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/api/regions")
async def get_regions():
    """Get available regions"""
    return {
        "regions": [
            {
                "id": "america",
                "name": "America",
                "countries": [
                    {"code": "US", "name": "United States"},
                    {"code": "CA", "name": "Canada"},
                    {"code": "MX", "name": "Mexico"}
                ]
            },
            {
                "id": "europe",
                "name": "Europe",
                "countries": [
                    {"code": "GB", "name": "United Kingdom"},
                    {"code": "DE", "name": "Germany"},
                    {"code": "FR", "name": "France"},
                    {"code": "IT", "name": "Italy"},
                    {"code": "ES", "name": "Spain"}
                ]
            },
            {
                "id": "asia",
                "name": "Asia",
                "countries": [
                    {"code": "IN", "name": "India"},
                    {"code": "CN", "name": "China"},
                    {"code": "JP", "name": "Japan"},
                    {"code": "SG", "name": "Singapore"},
                    {"code": "TH", "name": "Thailand"}
                ]
            }
        ]
    }


# Include routers (uncomment when routers are created)
# app.include_router(coupons.router, prefix="/api/coupons", tags=["coupons"])
# app.include_router(users.router, prefix="/api/users", tags=["users"])
# app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
# app.include_router(subscriptions.router, prefix="/api/subscriptions", tags=["subscriptions"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

