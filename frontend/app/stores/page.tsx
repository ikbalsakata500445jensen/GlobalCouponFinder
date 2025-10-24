'use client';

import { useSearchParams } from 'next/navigation';
import { StoreGrid } from '@/components/store/StoreGrid';
import { BannerAd } from '@/components/ads/BannerAd';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { useAppStore } from '@/store/appStore';

export default function StoresPage() {
  const searchParams = useSearchParams();
  const storeType = searchParams.get('store_type');
  const category = searchParams.get('category');
  const search = searchParams.get('search');
  const { region, country } = useAppStore();

  const getTitle = () => {
    if (storeType === 'food_delivery') return '🍔 Food Delivery Stores';
    if (category) return `Stores in ${category}`;
    if (search) return `Search Results for "${search}"`;
    return 'All Stores';
  };

  const getDescription = () => {
    if (storeType === 'food_delivery') return 'Find the best food delivery deals and coupons';
    if (category) return `Browse stores in the ${category} category`;
    if (search) return `Stores matching your search`;
    return 'Browse all available stores and find the best deals';
  };

  return (
    <div className="container px-4 py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold mb-2">{getTitle()}</h1>
        <p className="text-muted-foreground mb-4">{getDescription()}</p>
        
        {/* Active Filters */}
        <div className="flex flex-wrap gap-2">
          <Badge variant="secondary">
            Region: {region === 'america' ? '🌎 America' : region === 'europe' ? '🌍 Europe' : '🌏 Asia'}
          </Badge>
          {country && (
            <Badge variant="secondary">
              Country: {country}
            </Badge>
          )}
          {storeType && (
            <Badge variant="default">
              Type: {storeType.replace('_', ' ')}
            </Badge>
          )}
          {category && (
            <Badge variant="outline">
              Category: {category}
            </Badge>
          )}
        </div>
      </div>

      <BannerAd />

      <StoreGrid
        region={region}
        country={country || undefined}
        storeType={storeType || undefined}
        category={category || undefined}
        search={search || undefined}
        limit={50}
      />
    </div>
  );
}
