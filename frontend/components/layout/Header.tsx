'use client';

import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import { Search, User, LogOut } from 'lucide-react';
import { useAppStore } from '@/store/appStore';
import { useState } from 'react';
import { COUNTRIES } from '@/lib/countries';

export function Header() {
  const router = useRouter();
  const { user, region, country, setRegion, setCountry, logout } = useAppStore();
  const [searchInput, setSearchInput] = useState('');

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (searchInput.trim()) {
      router.push(`/search?q=${encodeURIComponent(searchInput)}`);
    }
  };

  const handleRegionChange = (value: string) => {
    setRegion(value as 'america' | 'europe' | 'asia');
    router.push(`/region/${value}`);
  };

  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-16 items-center justify-between px-4">
        {/* Logo */}
        <Link href="/" className="flex items-center space-x-2">
          <span className="text-2xl">🎫</span>
          <span className="font-bold text-xl hidden sm:inline">GlobalCouponFinder</span>
        </Link>

        {/* Search */}
        <form onSubmit={handleSearch} className="flex-1 max-w-md mx-4">
          <div className="relative">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
            <Input
              type="search"
              placeholder="Search stores or coupons..."
              value={searchInput}
              onChange={(e) => setSearchInput(e.target.value)}
              className="pl-10"
            />
          </div>
        </form>

        {/* Region & Country Selectors */}
        <div className="flex items-center gap-2">
          <Select value={region} onValueChange={handleRegionChange}>
            <SelectTrigger className="w-[140px]">
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="america">🌎 America</SelectItem>
              <SelectItem value="europe">🌍 Europe</SelectItem>
              <SelectItem value="asia">🌏 Asia</SelectItem>
            </SelectContent>
          </Select>

          <Select value={country || 'all'} onValueChange={(v) => setCountry(v === 'all' ? null : v)}>
            <SelectTrigger className="w-[140px]">
              <SelectValue placeholder="All Countries" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">All Countries</SelectItem>
              {COUNTRIES[region].map((c) => (
                <SelectItem key={c.code} value={c.code}>
                  {c.name}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>

        {/* User Menu */}
        <div className="flex items-center gap-2 ml-4">
          {user ? (
            <>
              <Button asChild variant="ghost" size="sm">
                <Link href="/dashboard">
                  <User className="w-4 h-4 mr-2" />
                  {user.full_name}
                </Link>
              </Button>
              <Button onClick={logout} variant="ghost" size="sm">
                <LogOut className="w-4 h-4" />
              </Button>
            </>
          ) : (
            <>
              <Button asChild variant="ghost" size="sm">
                <Link href="/login">Login</Link>
              </Button>
              <Button asChild variant="default" size="sm">
                <Link href="/register">Sign Up</Link>
              </Button>
            </>
          )}
        </div>
      </div>

      {/* Daily Limit Indicator (All Users) */}
      {user && (
        <div className="border-t bg-muted/50">
          <div className="container px-4 py-2">
            <div className="flex items-center justify-center text-sm">
              <span>
                Daily coupons used: {useAppStore((s) => s.dailyCouponCount)} / 50
              </span>
            </div>
          </div>
        </div>
      )}
    </header>
  );
}
