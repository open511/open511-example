from django.http import HttpResponse

def simple_index_page(request):
    return HttpResponse("""
<html>
<head><title>Open511 example</title></head>
<body>
<h1>Open511 example</h1>
<p>Browse the API starting at <a href="/api/">/api/</a>.</p>
<p>There's a rough administration interface at <a href="/admin/">/admin/</a>.</p>
<p>If you've installed the map UI software -- see the README -- you can <a href="/map/">visit that</a>.</p>
</body>
</html>
""", content_type='text/html')