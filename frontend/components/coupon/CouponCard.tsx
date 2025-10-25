'use client';

import { useState } from 'react';
import { Card, CardContent, CardFooter, CardHeader } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Copy, Check, ThumbsUp, ThumbsDown, ExternalLink } from 'lucide-react';
import { Coupon } from '@/types';
import { clickCoupon } from '@/lib/api';
import { useAppStore } from '@/store/appStore';
import { toast } from 'react-hot-toast';
import { format } from 'date-fns';

interface CouponCardProps {
  coupon: Coupon;
}

export function CouponCard({ coupon }: CouponCardProps) {
  const [copied, setCopied] = useState(false);
  const [loading, setLoading] = useState(false);
  const { user, incrementCouponCount, dailyCouponCount } = useAppStore();

  const handleCopyCode = async () => {
    // Check daily limit for all users
    if (dailyCouponCount >= 50) {
      toast.error('Daily limit reached! Come back tomorrow for more coupons.');
      return;
    }

    setLoading(true);
    try {
      // Track click and get affiliate URL
      const data = await clickCoupon(coupon.id);

      // Copy code to clipboard
      await navigator.clipboard.writeText(coupon.code);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);

      // Increment coupon count
      incrementCouponCount();

      // Open store in new tab
      window.open(data.affiliate_url, '_blank');

      toast.success('Code copied! Redirecting to store...');
    } catch (error) {
      toast.error('Failed to copy code');
    } finally {
      setLoading(false);
    }
  };

  const successRate =
    coupon.success_count + coupon.failure_count > 0
      ? Math.round(
          (coupon.success_count / (coupon.success_count + coupon.failure_count)) *
            100
        )
      : null;

  return (
    <Card className="hover:shadow-lg transition-shadow">
      <CardHeader>
        <div className="flex items-start justify-between">
          <div className="flex-1">
            <h3 className="font-semibold text-lg line-clamp-2">{coupon.title}</h3>
            <p className="text-sm text-muted-foreground mt-1">{coupon.store.name}</p>
          </div>
          {coupon.is_verified && (
            <Badge variant="secondary" className="ml-2">
              Verified
            </Badge>
          )}
        </div>
      </CardHeader>

      <CardContent>
        {coupon.description && (
          <p className="text-sm text-muted-foreground mb-4 line-clamp-2">
            {coupon.description}
          </p>
        )}

        <div className="flex items-center gap-2 mb-4">
          {coupon.discount_value && (
            <Badge variant="default" className="text-lg">
              {coupon.discount_type === 'percentage'
                ? `${coupon.discount_value}% OFF`
                : `$${coupon.discount_value} OFF`}
            </Badge>
          )}
          {coupon.discount_type === 'free_shipping' && (
            <Badge variant="secondary">FREE SHIPPING</Badge>
          )}
        </div>

        <div className="space-y-2 text-sm">
          {coupon.expires_at && (
            <div className="flex items-center gap-2 text-muted-foreground">
              <span>Expires: {format(new Date(coupon.expires_at), 'MMM dd, yyyy')}</span>
            </div>
          )}

          {successRate !== null && (
            <div className="flex items-center gap-2">
              <div className="flex items-center gap-1">
                <ThumbsUp className="w-4 h-4 text-green-600" />
                <span className="text-green-600 font-medium">{successRate}% success</span>
              </div>
              <span className="text-muted-foreground">
                ({coupon.success_count + coupon.failure_count} uses)
              </span>
            </div>
          )}
        </div>
      </CardContent>

      <CardFooter>
        <Button
          onClick={handleCopyCode}
          disabled={loading}
          className="w-full"
          size="lg"
        >
          {copied ? (
            <>
              <Check className="w-4 h-4 mr-2" />
              Copied!
            </>
          ) : (
            <>
              <Copy className="w-4 h-4 mr-2" />
              Copy Code: {coupon.code}
            </>
          )}
        </Button>
      </CardFooter>
    </Card>
  );
}
