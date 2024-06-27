document.addEventListener("DOMContentLoaded", function () {
    const agregarAlCarritoButtons = document.querySelectorAll(
      ".agregar-al-carrito"
    );
    agregarAlCarritoButtons.forEach((button) => {
      button.addEventListener("click", agregarAlCarrito);
    });
  
    const carrito = document.getElementById("articulos-en-carrito");
    carrito.addEventListener("click", eliminarDelCarrito);
  
    function agregarAlCarrito(event) {
      const button = event.target;
      const product = button.parentElement;
      const productTitle = product.querySelector("h2").textContent;
      const productPrice = product
        .querySelector("span")
        .getAttribute("data-precio");
  
      agregarItemAlCarrito(productTitle, productPrice);
    }
  
    function agregarItemAlCarrito(productTitle, productPrice) {
      const carritoItem = document.createElement("li");
      carritoItem.classList.add("carrito-item");
      const carritoItemContent = `
            <span>${productTitle} - Precio: $${productPrice}</span>
            <button class="eliminar-del-carrito">Eliminar</button>
        `;
      carritoItem.innerHTML = carritoItemContent;
      carrito.appendChild(carritoItem);
  
      calcularSubtotal();
    }
  
    function calcularSubtotal() {
      const carritoItems = carrito.querySelectorAll(".carrito-item");
      let subtotal = 0;
      carritoItems.forEach((item) => {
        const price = parseFloat(
          item.querySelector("span").textContent.split("$")[1]
        );
        subtotal += price;
      });
      document.getElementById("subtotal").textContent = subtotal.toFixed(2);
    }
  
    function eliminarDelCarrito(event) {
      if (event.target.classList.contains("eliminar-del-carrito")) {
        const button = event.target;
        button.parentElement.remove();
        calcularSubtotal();
      }
    }
  });