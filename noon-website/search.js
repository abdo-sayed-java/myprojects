document.addEventListener("DOMContentLoaded", async () => {
  const searchResults = document.getElementById("searchResults");
  const query = localStorage.getItem("searchQuery")?.toLowerCase() || "";

  if (!query) {
    searchResults.innerHTML = "<p>Please enter a search term.</p>";
    return;
  }

  try {
    const response = await fetch("https://dummyjson.com/products");
    const data = await response.json();
    const products = data.products;

    // Filter products
    const filtered = products.filter(product =>
      product.title.toLowerCase().includes(query)
    );

    if (filtered.length === 0) {
      searchResults.innerHTML = `<p>No products found for "<strong>${query}</strong>".</p>`;
      return;
    }

    searchResults.innerHTML = `<h2>Results for "<strong>${query}</strong>":</h2>
      <div id="productList"></div>`;

    const productList = document.getElementById("productList");

    filtered.forEach(product => {
      const productDiv = document.createElement("div");
      productDiv.className = "product";
      productDiv.innerHTML = `
        <img src="${product.images[0]}" alt="product image" class="product-image">
        <h3>${product.title}</h3>
        <p class="price">Price: $${product.price}</p>
        <p class="stock">Stock: ${product.stock}</p>
        <button class="buy-btn">Buy Now</button>
      `;
      productDiv.addEventListener("click", () => {
        localStorage.setItem("selectedProduct", JSON.stringify(product));
        window.location.href = "product.html";
      });
      productList.appendChild(productDiv);
    });
  } catch (error) {
    searchResults.innerHTML = `<p style="color:red;">Error: ${error.message}</p>`;
  }
});