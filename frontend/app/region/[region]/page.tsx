'use client';

import { useParams } from 'next/navigation';
import { CouponGrid } from '@/components/coupon/CouponGrid';
import { StoreGrid } from '@/components/store/StoreGrid';
import { BannerAd } from '@/components/ads/BannerAd';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Button } from '@/components/ui/button';
import Link from 'next/link';

export default function RegionPage() {
  const params = useParams();
  const region = params.region as string;

  const getRegionInfo = (region: string) => {
    switch (region) {
      case 'america':
        return {
          name: 'America',
          icon: '🌎',
          description: 'Find coupons from stores across North and South America',
          stores: '40+ stores',
          countries: ['US', 'CA', 'MX', 'BR']
        };
      case 'europe':
        return {
          name: 'Europe',
          icon: '🌍',
          description: 'Discover deals from European retailers and services',
          stores: '35+ stores',
          countries: ['GB', 'DE', 'FR', 'ES', 'IT', 'NL', 'PL']
        };
      case 'asia':
        return {
          name: 'Asia',
          icon: '🌏',
          description: 'Explore coupons from Asian markets and platforms',
          stores: '35+ stores',
          countries: ['SG', 'MY', 'TH', 'PH', 'ID', 'VN', 'IN', 'CN', 'JP', 'KR']
        };
      default:
        return {
          name: 'All Regions',
          icon: '🌍',
          description: 'Browse all available stores and coupons',
          stores: '100+ stores',
          countries: []
        };
    }
  };

  const regionInfo = getRegionInfo(region);

  return (
    <div className="container px-4 py-8">
      {/* Hero Section */}
      <section className="text-center py-12 mb-8">
        <div className="text-6xl mb-4">{regionInfo.icon}</div>
        <h1 className="text-4xl font-bold mb-4">{regionInfo.name} Coupons</h1>
        <p className="text-xl text-muted-foreground mb-8 max-w-2xl mx-auto">
          {regionInfo.description}
        </p>
        <div className="flex flex-wrap justify-center gap-4">
          <Button asChild size="lg">
            <Link href={`/stores?store_type=food_delivery&region=${region}`}>
              🍔 Food Delivery
            </Link>
          </Button>
          <Button asChild size="lg" variant="outline">
            <Link href={`/stores?region=${region}`}>
              Browse All Stores
            </Link>
          </Button>
        </div>
      </section>

      <BannerAd />

      {/* Tabs: Coupons / Stores */}
      <Tabs defaultValue="coupons" className="mb-8">
        <TabsList className="grid w-full grid-cols-2 max-w-md mx-auto">
          <TabsTrigger value="coupons">Latest Coupons</TabsTrigger>
          <TabsTrigger value="stores">Popular Stores</TabsTrigger>
        </TabsList>

        <TabsContent value="coupons" className="mt-6">
          <CouponGrid region={region} limit={20} />
        </TabsContent>

        <TabsContent value="stores" className="mt-6">
          <StoreGrid region={region} limit={20} />
        </TabsContent>
      </Tabs>

      {/* Food Delivery Section */}
      <section className="mb-12">
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-3xl font-bold">🚚 Food Delivery in {regionInfo.name}</h2>
          <Button asChild variant="outline">
            <Link href={`/stores?store_type=food_delivery&region=${region}`}>
              View All
            </Link>
          </Button>
        </div>
        <StoreGrid region={region} storeType="food_delivery" limit={8} />
      </section>

      <BannerAd />

      {/* Countries in Region */}
      <section className="mb-12">
        <h2 className="text-3xl font-bold mb-6">Countries in {regionInfo.name}</h2>
        <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
          {regionInfo.countries.map((countryCode) => (
            <Button
              key={countryCode}
              asChild
              variant="outline"
              className="h-auto p-4 flex flex-col items-center space-y-2"
            >
              <Link href={`/stores?region=${region}&country=${countryCode}`}>
                <span className="text-2xl">
                  {countryCode === 'US' && '🇺🇸'}
                  {countryCode === 'CA' && '🇨🇦'}
                  {countryCode === 'MX' && '🇲🇽'}
                  {countryCode === 'BR' && '🇧🇷'}
                  {countryCode === 'GB' && '🇬🇧'}
                  {countryCode === 'DE' && '🇩🇪'}
                  {countryCode === 'FR' && '🇫🇷'}
                  {countryCode === 'ES' && '🇪🇸'}
                  {countryCode === 'IT' && '🇮🇹'}
                  {countryCode === 'NL' && '🇳🇱'}
                  {countryCode === 'PL' && '🇵🇱'}
                  {countryCode === 'SG' && '🇸🇬'}
                  {countryCode === 'MY' && '🇲🇾'}
                  {countryCode === 'TH' && '🇹🇭'}
                  {countryCode === 'PH' && '🇵🇭'}
                  {countryCode === 'ID' && '🇮🇩'}
                  {countryCode === 'VN' && '🇻🇳'}
                  {countryCode === 'IN' && '🇮🇳'}
                  {countryCode === 'CN' && '🇨🇳'}
                  {countryCode === 'JP' && '🇯🇵'}
                  {countryCode === 'KR' && '🇰🇷'}
                </span>
                <span className="text-sm font-medium">{countryCode}</span>
              </Link>
            </Button>
          ))}
        </div>
      </section>
    </div>
  );
}
