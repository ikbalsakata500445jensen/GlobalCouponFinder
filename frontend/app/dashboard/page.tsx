'use client';

import { useAppStore } from '@/store/appStore';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { CouponGrid } from '@/components/coupon/CouponGrid';
import { BannerAd } from '@/components/ads/BannerAd';
import { Crown, User, MapPin, Calendar, Zap } from 'lucide-react';
import Link from 'next/link';

export default function DashboardPage() {
  const { user, dailyCouponCount } = useAppStore();

  if (!user) {
    return (
      <div className="container px-4 py-8">
        <div className="text-center">
          <h1 className="text-2xl font-bold mb-4">Please sign in</h1>
          <p className="text-muted-foreground mb-6">
            You need to be signed in to access your dashboard.
          </p>
          <Button asChild>
            <Link href="/login">Sign In</Link>
          </Button>
        </div>
      </div>
    );
  }

  return (
    <div className="container px-4 py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold mb-2">Welcome back, {user.full_name}!</h1>
        <p className="text-muted-foreground">
          Here's your personalized dashboard with the latest deals and your activity.
        </p>
      </div>

      {/* User Stats */}
      <div className="grid md:grid-cols-3 gap-6 mb-8">
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Account Status</CardTitle>
            <User className="h-4 w-4" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">
              Free
            </div>
            <p className="text-xs text-muted-foreground">
              Limited to 50 coupons/day
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Daily Usage</CardTitle>
            <Zap className="h-4 w-4" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">
              {dailyCouponCount} / 50
            </div>
            <p className="text-xs text-muted-foreground">
              Coupons used today
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Location</CardTitle>
            <MapPin className="h-4 w-4" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">
              {user.region === 'america' ? '🌎' : user.region === 'europe' ? '🌍' : '🌏'} {user.region}
            </div>
            <p className="text-xs text-muted-foreground">
              {user.country}
            </p>
          </CardContent>
        </Card>
      </div>

      {/* Daily Limit Info */}
      <Card className="mb-8 border-blue-200 bg-blue-50">
        <CardContent className="pt-6">
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-lg font-semibold text-blue-800">
                Daily Coupon Limit
              </h3>
              <p className="text-blue-700">
                You can use up to 50 coupons per day. Limit resets at midnight.
              </p>
            </div>
            <div className="text-right">
              <div className="text-2xl font-bold text-blue-800">
                {dailyCouponCount} / 50
              </div>
              <p className="text-sm text-blue-600">Used today</p>
            </div>
          </div>
        </CardContent>
      </Card>

      <BannerAd />

      {/* Latest Coupons */}
      <section className="mb-8">
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-2xl font-bold">Latest Coupons for You</h2>
          <Button asChild variant="outline">
            <Link href="/">View All</Link>
          </Button>
        </div>
        <CouponGrid limit={12} />
      </section>

      {/* Quick Actions */}
      <section className="mb-8">
        <h2 className="text-2xl font-bold mb-6">Quick Actions</h2>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <Button asChild variant="outline" className="h-auto p-6 flex flex-col items-center space-y-2">
            <Link href="/stores?store_type=food_delivery">
              <span className="text-2xl">🍔</span>
              <span>Food Delivery</span>
            </Link>
          </Button>
          
          <Button asChild variant="outline" className="h-auto p-6 flex flex-col items-center space-y-2">
            <Link href="/stores?category=fashion">
              <span className="text-2xl">👗</span>
              <span>Fashion</span>
            </Link>
          </Button>
          
          <Button asChild variant="outline" className="h-auto p-6 flex flex-col items-center space-y-2">
            <Link href="/stores?category=electronics">
              <span className="text-2xl">💻</span>
              <span>Electronics</span>
            </Link>
          </Button>
          
          <Button asChild variant="outline" className="h-auto p-6 flex flex-col items-center space-y-2">
            <Link href="/search">
              <span className="text-2xl">🔍</span>
              <span>Search</span>
            </Link>
          </Button>
        </div>
      </section>
    </div>
  );
}
