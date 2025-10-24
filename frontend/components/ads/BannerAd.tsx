'use client';

export function BannerAd() {
  // Always show ads to all users (no premium features)
  return (
    <div className="w-full flex justify-center my-4 p-4 bg-muted rounded-lg border-2 border-dashed">
      <div className="text-center text-muted-foreground">
        <p className="text-sm">📢 Ad Space</p>
        <p className="text-xs">AdMob integration ready for production</p>
      </div>
    </div>
  );
}
