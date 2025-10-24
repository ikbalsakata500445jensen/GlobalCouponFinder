'use client';

import { useQuery } from '@tanstack/react-query';
import { getCoupons } from '@/lib/api';
import { CouponCard } from './CouponCard';
import { Skeleton } from '@/components/ui/skeleton';
import { useAppStore } from '@/store/appStore';
import { BannerAd } from '@/components/ads/BannerAd';

interface CouponGridProps {
  region?: string;
  country?: string;
  storeId?: number;
  category?: string;
  search?: string;
  limit?: number;
}

export function CouponGrid({
  region,
  country,
  storeId,
  category,
  search,
  limit = 20,
}: CouponGridProps) {
  const globalRegion = useAppStore((state) => state.region);
  const globalCountry = useAppStore((state) => state.country);

  const { data, isLoading, error } = useQuery({
    queryKey: [
      'coupons',
      region || globalRegion,
      country || globalCountry,
      storeId,
      category,
      search,
    ],
    queryFn: () =>
      getCoupons({
        region: region || globalRegion,
        country: country || globalCountry || undefined,
        store_id: storeId,
        category,
        search,
        limit,
      }),
  });

  if (isLoading) {
    return (
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {Array.from({ length: limit }).map((_, i) => (
          <Skeleton key={i} className="h-64" />
        ))}
      </div>
    );
  }

  if (error) {
    return (
      <div className="text-center py-12">
        <p className="text-red-500">Failed to load coupons</p>
      </div>
    );
  }

  if (!data?.coupons || data.coupons.length === 0) {
    return (
      <div className="text-center py-12">
        <p className="text-muted-foreground">No coupons found</p>
      </div>
    );
  }

  return (
    <div className="space-y-8">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {data.coupons.map((coupon, index) => (
          <>
            <CouponCard key={coupon.id} coupon={coupon} />
            {/* Insert native ad every 6 coupons */}
            {(index + 1) % 6 === 0 && <BannerAd />}
          </>
        ))}
      </div>
    </div>
  );
}
