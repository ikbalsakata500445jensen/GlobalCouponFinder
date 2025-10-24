'use client';

import Link from 'next/link';
import { Card } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Store } from '@/types';

interface StoreCardProps {
  store: Store;
}

export function StoreCard({ store }: StoreCardProps) {
  return (
    <Link href={`/stores/${store.slug}`}>
      <Card className="p-4 hover:shadow-lg transition-shadow cursor-pointer h-full">
        <div className="flex flex-col items-center text-center space-y-2">
          {/* Store Logo */}
          {store.logo_url ? (
            <img
              src={store.logo_url}
              alt={store.name}
              className="w-16 h-16 object-contain"
            />
          ) : (
            <div className="w-16 h-16 bg-muted rounded flex items-center justify-center">
              <span className="text-2xl">🏪</span>
            </div>
          )}

          {/* Store Name */}
          <h3 className="font-semibold text-sm line-clamp-2">{store.name}</h3>

          {/* Coupon Count */}
          <Badge variant="secondary" className="text-xs">
            {store.active_coupons_count} coupons
          </Badge>

          {/* Store Type Badge */}
          {store.store_type === 'food_delivery' && (
            <Badge variant="default" className="text-xs">
              🍔 Food Delivery
            </Badge>
          )}
        </div>
      </Card>
    </Link>
  );
}
