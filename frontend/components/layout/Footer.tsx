import Link from 'next/link';

export function Footer() {
  return (
    <footer className="border-t bg-muted/50 mt-12">
      <div className="container px-4 py-8">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
          {/* About */}
          <div>
            <h3 className="font-semibold mb-4">About</h3>
            <ul className="space-y-2 text-sm text-muted-foreground">
              <li>
                <Link href="/about" className="hover:text-foreground">
                  About Us
                </Link>
              </li>
              <li>
                <Link href="/contact" className="hover:text-foreground">
                  Contact
                </Link>
              </li>
              <li>
                <Link href="/blog" className="hover:text-foreground">
                  Blog
                </Link>
              </li>
            </ul>
          </div>

          {/* Regions */}
          <div>
            <h3 className="font-semibold mb-4">Regions</h3>
            <ul className="space-y-2 text-sm text-muted-foreground">
              <li>
                <Link href="/region/america" className="hover:text-foreground">
                  🌎 America
                </Link>
              </li>
              <li>
                <Link href="/region/europe" className="hover:text-foreground">
                  🌍 Europe
                </Link>
              </li>
              <li>
                <Link href="/region/asia" className="hover:text-foreground">
                  🌏 Asia
                </Link>
              </li>
            </ul>
          </div>

          {/* Categories */}
          <div>
            <h3 className="font-semibold mb-4">Categories</h3>
            <ul className="space-y-2 text-sm text-muted-foreground">
              <li>
                <Link
                  href="/stores?store_type=food_delivery"
                  className="hover:text-foreground"
                >
                  Food Delivery
                </Link>
              </li>
              <li>
                <Link href="/categories/fashion" className="hover:text-foreground">
                  Fashion
                </Link>
              </li>
              <li>
                <Link
                  href="/categories/electronics"
                  className="hover:text-foreground"
                >
                  Electronics
                </Link>
              </li>
              <li>
                <Link href="/stores" className="hover:text-foreground">
                  All Stores
                </Link>
              </li>
            </ul>
          </div>

          {/* Legal */}
          <div>
            <h3 className="font-semibold mb-4">Legal</h3>
            <ul className="space-y-2 text-sm text-muted-foreground">
              <li>
                <Link href="/privacy" className="hover:text-foreground">
                  Privacy Policy
                </Link>
              </li>
              <li>
                <Link href="/terms" className="hover:text-foreground">
                  Terms of Service
                </Link>
              </li>
              <li>
                <Link href="/premium" className="hover:text-foreground">
                  Premium
                </Link>
              </li>
            </ul>
          </div>
        </div>

        <div className="border-t mt-8 pt-8 text-center text-sm text-muted-foreground">
          <p>
            © {new Date().getFullYear()} GlobalCouponFinder. All rights reserved.
          </p>
          <p className="mt-2">
            Find coupons from 100+ stores across America, Europe & Asia 🌍
          </p>
        </div>
      </div>
    </footer>
  );
}
