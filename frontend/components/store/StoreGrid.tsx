'use client';

import { useQuery } from '@tanstack/react-query';
import { getStores } from '@/lib/api';
import { StoreCard } from './StoreCard';
import { Skeleton } from '@/components/ui/skeleton';
import { useAppStore } from '@/store/appStore';

interface StoreGridProps {
  region?: string;
  country?: string;
  storeType?: string;
  category?: string;
  search?: string;
  limit?: number;
}

export function StoreGrid({
  region,
  country,
  storeType,
  category,
  search,
  limit = 20,
}: StoreGridProps) {
  const globalRegion = useAppStore((state) => state.region);
  const globalCountry = useAppStore((state) => state.country);

  const { data, isLoading, error } = useQuery({
    queryKey: [
      'stores',
      region || globalRegion,
      country || globalCountry,
      storeType,
      category,
      search,
    ],
    queryFn: () =>
      getStores({
        region: region || globalRegion,
        country: country || globalCountry || undefined,
        store_type: storeType,
        category,
        search,
        limit,
      }),
  });

  if (isLoading) {
    return (
      <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
        {Array.from({ length: limit }).map((_, i) => (
          <Skeleton key={i} className="h-32" />
        ))}
      </div>
    );
  }

  if (error) {
    return (
      <div className="text-center py-12">
        <p className="text-red-500">Failed to load stores</p>
      </div>
    );
  }

  if (!data?.stores || data.stores.length === 0) {
    return (
      <div className="text-center py-12">
        <p className="text-muted-foreground">No stores found</p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
      {data.stores.map((store) => (
        <StoreCard key={store.id} store={store} />
      ))}
    </div>
  );
}
