/** @type {import('next').NextConfig} */

const nextConfig = {
output: 'export',
trailingSlash: true,
images: {
unoptimized: true
},
basePath: '/ChatKie',
assetPrefix: '/ChatKie/'
};

export default nextConfig;
