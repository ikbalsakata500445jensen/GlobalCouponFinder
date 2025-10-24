'use client';

import { useSearchParams } from 'next/navigation';
import { CouponGrid } from '@/components/coupon/CouponGrid';
import { StoreGrid } from '@/components/store/StoreGrid';
import { BannerAd } from '@/components/ads/BannerAd';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';

export default function SearchPage() {
  const searchParams = useSearchParams();
  const query = searchParams.get('q') || '';

  return (
    <div className="container px-4 py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold mb-2">
          Search Results for "{query}"
        </h1>
        <p className="text-muted-foreground">
          Find the best coupons and deals for your search
        </p>
      </div>

      <BannerAd />

      <Tabs defaultValue="coupons" className="mb-8">
        <TabsList className="grid w-full grid-cols-2 max-w-md">
          <TabsTrigger value="coupons">Coupons</TabsTrigger>
          <TabsTrigger value="stores">Stores</TabsTrigger>
        </TabsList>

        <TabsContent value="coupons" className="mt-6">
          <CouponGrid search={query} limit={20} />
        </TabsContent>

        <TabsContent value="stores" className="mt-6">
          <StoreGrid search={query} limit={20} />
        </TabsContent>
      </Tabs>
    </div>
  );
}
