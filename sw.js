const CACHE = 'akitime-v1';
const APP_FILES = ['./','./index.html','./manifest.json','./icon.svg'];

self.addEventListener('install', e => {
    e.waitUntil(
        caches.open(CACHE).then(c => c.addAll(APP_FILES)).then(() => self.skipWaiting())
    );
});

self.addEventListener('activate', e => {
    e.waitUntil(
        caches.keys().then(keys =>
            Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
        ).then(() => self.clients.claim())
    );
});

self.addEventListener('fetch', e => {
    const url = e.request.url;
    // Microsoft APIは常にネットワーク（キャッシュしない）
    if (url.includes('microsoftonline.com') || url.includes('graph.microsoft.com') || url.includes('msauth.net')) {
        return;
    }
    // アプリ本体はネットワーク優先→失敗時キャッシュ
    e.respondWith(
        fetch(e.request).catch(() => caches.match(e.request))
    );
});
