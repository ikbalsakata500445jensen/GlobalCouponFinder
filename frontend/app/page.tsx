import { CouponGrid } from '@/components/coupon/CouponGrid';
import { StoreGrid } from '@/components/store/StoreGrid';
import { BannerAd } from '@/components/ads/BannerAd';
import { Button } from '@/components/ui/button';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import Link from 'next/link';

export default function HomePage() {
  return (
    <div className="container px-4 py-8">
      {/* Hero Section */}
      <section className="text-center py-12 mb-8">
        <h1 className="text-4xl md:text-5xl font-bold mb-4">
          Find Coupons Around The World 🌍
        </h1>
        <p className="text-xl text-muted-foreground mb-8 max-w-2xl mx-auto">
          100+ stores from America, Europe & Asia. Food delivery, shopping, and more!
        </p>
        <div className="flex flex-wrap justify-center gap-4">
          <Button asChild size="lg">
            <Link href="/stores?store_type=food_delivery">
              🍔 Food Delivery Coupons
            </Link>
          </Button>
          <Button asChild size="lg" variant="outline">
            <Link href="/stores">Browse All Stores</Link>
          </Button>
        </div>
      </section>

      {/* Banner Ad */}
      <BannerAd />

      {/* Tabs: Latest Coupons / Popular Stores */}
      <Tabs defaultValue="coupons" className="mb-8">
        <TabsList className="grid w-full grid-cols-2 max-w-md mx-auto">
          <TabsTrigger value="coupons">Latest Coupons</TabsTrigger>
          <TabsTrigger value="stores">Popular Stores</TabsTrigger>
        </TabsList>

        <TabsContent value="coupons" className="mt-6">
          <CouponGrid limit={12} />
        </TabsContent>

        <TabsContent value="stores" className="mt-6">
          <StoreGrid limit={12} />
        </TabsContent>
      </Tabs>

      {/* Food Delivery Section */}
      <section className="mb-12">
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-3xl font-bold">🚚 Food Delivery Deals</h2>
          <Button asChild variant="outline">
            <Link href="/stores?store_type=food_delivery">View All</Link>
          </Button>
        </div>
        <StoreGrid storeType="food_delivery" limit={8} />
      </section>

      {/* Banner Ad */}
      <BannerAd />

      {/* Categories Section */}
      <section className="mb-12">
        <h2 className="text-3xl font-bold mb-6">Shop by Category</h2>
        <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
          {[
            { name: 'Fashion', icon: '👗', slug: 'fashion' },
            { name: 'Electronics', icon: '💻', slug: 'electronics' },
            { name: 'Beauty', icon: '💄', slug: 'beauty' },
            { name: 'Food', icon: '🍔', slug: 'food-delivery' },
            { name: 'Home', icon: '🏡', slug: 'home-garden' },
            { name: 'Sports', icon: '⚽', slug: 'sports' },
          ].map((category) => (
            <Link
              key={category.slug}
              href={`/categories/${category.slug}`}
              className="flex flex-col items-center justify-center p-6 border rounded-lg hover:shadow-lg transition-shadow"
            >
              <span className="text-4xl mb-2">{category.icon}</span>
              <span className="font-medium">{category.name}</span>
            </Link>
          ))}
        </div>
      </section>

      {/* Regional Sections */}
      <section className="mb-12">
        <h2 className="text-3xl font-bold mb-6">Browse by Region</h2>
        <div className="grid md:grid-cols-3 gap-6">
          {[
            { name: 'America', icon: '🌎', region: 'america', stores: '40+' },
            { name: 'Europe', icon: '🌍', region: 'europe', stores: '35+' },
            { name: 'Asia', icon: '🌏', region: 'asia', stores: '35+' },
          ].map((region) => (
            <Link
              key={region.region}
              href={`/region/${region.region}`}
              className="p-8 border rounded-lg hover:shadow-lg transition-shadow text-center"
            >
              <div className="text-6xl mb-4">{region.icon}</div>
              <h3 className="text-2xl font-bold mb-2">{region.name}</h3>
              <p className="text-muted-foreground">{region.stores} stores</p>
            </Link>
          ))}
        </div>
      </section>
    </div>
  );
}
