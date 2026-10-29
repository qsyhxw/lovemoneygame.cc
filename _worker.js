// Keep recoverable maintenance sources out of the public website.
export default {
  async fetch(request, env) {
    const path = decodeURIComponent(new URL(request.url).pathname);
    if (/^\/(?:scripts|config|_private|outputs|PAGE_REPORTS)(?:\/|$)/i.test(path) || /\.(?:md|py)$/i.test(path)) {
      return new Response('Not found', { status: 404, headers: { 'Content-Type': 'text/plain; charset=utf-8', 'X-Robots-Tag': 'noindex' } });
    }
    return env.ASSETS.fetch(request);
  }
};
