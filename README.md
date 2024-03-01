<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!--<title>README</title>
</head>
<body>

<h1>Installation</h1>
<ol>
<li>Clone the repository:
<pre><code>git clone &lt;repository_url&gt;</code></pre></li>
<li>Run Docker Compose
<pre><code>docker-compose up --build</code></pre></li>
</ol>-->

<h2>Model</h2>
<p><img src="model.png" alt="Model"></p>

<h2>Endpoints</h2>
<ul>
<li>Products Endpoint: <a href="http://127.0.0.1:8000/inventory/products">http://127.0.0.1:8000/inventory/products</a></li>
<li>Bulk Products Endpoint: <a href="http://127.0.0.1:8000/inventory/products-bulk">http://127.0.0.1:8000/inventory/products-bulk</a></li>
</ul>

<h2>Tests</h2>
<p>Run tests using the following command:</p>
<pre><code>python manage.py test</code></pre>

<h3>Solution 1: Sequential Insertion</h3>
<p>Insert all products and their variants using the <code>create</code> method sequentially.</p>
<p>Endpoint: <a href="http://127.0.0.1:8000/inventory/products">http://127.0.0.1:8000/inventory/products</a></p>
<p>Test Results:</p>
<p><img src="create.png" alt="Create Method"></p>

<h3>Solution 2: Bulk Insertion</h3>
<p>Insert products and their variants using the <code>bulk_create</code> method.</p>
<p>Endpoint: <a href="http://127.0.0.1:8000/inventory/products-bulk">http://127.0.0.1:8000/inventory/products-bulk</a></p>
<p>Test Results:</p>
<p><img src="bulk.png" alt="Bulk Create Method"></p>
<h3>Analysis</h3>

<p>Solution 2 Bulk Insertion is a more efficient method for large datasets in terms of execution time.</p>

</body>
</html>
