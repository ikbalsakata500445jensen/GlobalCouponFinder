import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import { User } from '@/types';

interface AppState {
  // User
  user: User | null;
  token: string | null;
  setUser: (user: User | null) => void;
  setToken: (token: string | null) => void;
  logout: () => void;

  // Filters
  region: 'america' | 'europe' | 'asia';
  country: string | null;
  searchQuery: string;
  setRegion: (region: 'america' | 'europe' | 'asia') => void;
  setCountry: (country: string | null) => void;
  setSearchQuery: (query: string) => void;

  // Coupon count
  dailyCouponCount: number;
  incrementCouponCount: () => void;
  resetCouponCount: () => void;

  // Ad control
  showInterstitial: boolean;
  setShowInterstitial: (show: boolean) => void;
}

export const useAppStore = create<AppState>()(
  persist(
    (set, get) => ({
      // User
      user: null,
      token: null,
      setUser: (user) => set({ user }),
      setToken: (token) => {
        set({ token });
        if (token) {
          localStorage.setItem('token', token);
        } else {
          localStorage.removeItem('token');
        }
      },
      logout: () => {
        set({ user: null, token: null });
        localStorage.removeItem('token');
      },

      // Filters
      region: 'america',
      country: null,
      searchQuery: '',
      setRegion: (region) => set({ region, country: null }),
      setCountry: (country) => set({ country }),
      setSearchQuery: (searchQuery) => set({ searchQuery }),

      // Coupon count
      dailyCouponCount: 0,
      incrementCouponCount: () => {
        const count = get().dailyCouponCount + 1;
        set({ dailyCouponCount: count });
        
        // Show interstitial ad every 3 coupons for all users
        if (count % 3 === 0) {
          set({ showInterstitial: true });
        }
      },
      resetCouponCount: () => set({ dailyCouponCount: 0 }),

      // Ad control
      showInterstitial: false,
      setShowInterstitial: (show) => set({ showInterstitial: show }),
    }),
    {
      name: 'globalcouponfinder-storage',
      partialize: (state) => ({
        token: state.token,
        region: state.region,
        country: state.country,
        dailyCouponCount: state.dailyCouponCount,
      }),
    }
  )
);
