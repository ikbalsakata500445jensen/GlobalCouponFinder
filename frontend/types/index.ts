export interface User {
  id: string;
  email: string;
  full_name: string;
  is_premium: boolean;
  region: 'america' | 'europe' | 'asia';
  country: string;
  daily_coupon_count: number;
}

export interface Store {
  id: number;
  name: string;
  slug: string;
  domain: string;
  logo_url?: string;
  region: 'america' | 'europe' | 'asia';
  country: string;
  store_type: 'retail' | 'food_delivery' | 'grocery';
  category: string;
  active_coupons_count: number;
}

export interface Coupon {
  id: string;
  store_id: number;
  code: string;
  title: string;
  description?: string;
  discount_type: 'percentage' | 'fixed' | 'free_shipping' | 'bogo';
  discount_value?: number;
  minimum_purchase?: number;
  expires_at?: string;
  success_count: number;
  failure_count: number;
  view_count: number;
  click_count: number;
  is_verified: boolean;
  is_exclusive: boolean;
  store: Store;
}

export interface Category {
  id: number;
  name: string;
  slug: string;
  icon: string;
}

export interface Country {
  code: string;
  name: string;
}

export interface PaginatedResponse<T> {
  data: T[];
  total: number;
  page: number;
  pages: number;
}
