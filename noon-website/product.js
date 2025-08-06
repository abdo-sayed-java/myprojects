document.addEventListener("DOMContentLoaded", () => {
  const productDetails = document.getElementById("productDetails");
  const product = JSON.parse(localStorage.getItem("selectedProduct"));

  if (!product) {
    productDetails.innerHTML = "<p>Product not found.</p>";
    return;
  }

  productDetails.innerHTML = `
    <div class="product-details-card">
      <img src="${product.images[0]}" alt="${product.title}" class="product-details-image">
      <div class="product-details-info">
        <h2>${product.title}</h2>
        <p class="price">Price: $${product.price}</p>
        <p class="stock">Stock: ${product.stock}</p>
        <p class="description">${product.description}</p>
        <button class="buy-btn">Buy Now</button>
      </div>
    </div>
  `;
});