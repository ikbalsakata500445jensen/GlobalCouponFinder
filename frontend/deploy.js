const { execSync } = require('child_process');

console.log('🚀 Deploying GlobalCouponFinder to Vercel...');

try {
  // Build the project
  console.log('📦 Building project...');
  execSync('npm run build', { stdio: 'inherit' });
  
  console.log('✅ Build successful!');
  console.log('🌐 Deploying to Vercel...');
  
  // Deploy to Vercel
  execSync('npx vercel --prod --yes', { stdio: 'inherit' });
  
  console.log('🎉 Deployment successful!');
} catch (error) {
  console.error('❌ Deployment failed:', error.message);
  process.exit(1);
}
