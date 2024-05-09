import React, { useState, useEffect, useContext } from 'react';
import { CartContext } from './CartContext';
import './Shastar.css'; // Replace 'YourCSSFileName' with the actual name of your CSS file

function Shastars() {
  const [shastars, setShastars] = useState([]);
  const { addToCart } = useContext(CartContext); // Access addToCart function from CartContext

  useEffect(() => {
    fetch('http://127.0.0.1:5555/shastars')
      .then(response => response.json())
      .then(data => {
        console.log(data);
        setShastars(data);
      });
  }, []);

  // const handleDeleteShastar = id => {
  //   console.log("Shastars before deletion:", shastars);
  //   fetch(`/shastars/${id}`, {
  //     method: 'DELETE',
  //   })
  //     .then(() => {
  //       setShastars(shastars.filter(shastar => shastar.id !== id));
  //       console.log("Shastars after deletion:", shastars);
  //     });
  // };

  const handleAddToCart = (shastar) => {
    addToCart(shastar); // Call addToCart function from CartContext
    console.log("Added to cart:", shastar);
  };
  
  return (
    <div className="shastar-container">
      <h2>Shastars</h2>
      {shastars.map(shastar => (
        <div key={shastar.id} className="card">
          <div className="card-image-container">
            <img src={shastar.image_url} alt={shastar.name} className="card-image" />
          </div >
          <div className="info-container">
          <div className="card-title">{shastar.name}</div>
          <div className="card-des">{shastar.description}</div>
          <div className="card-price">Price: ${shastar.price}</div>
          {/* <button onClick={() => handleDeleteShastar(shastar.id)}>Delete</button> */}
          <button onClick={() => handleAddToCart(shastar)} className="add-to-cart-button">Add to Cart</button> {/* Add button to add shastar to cart */}
        </div>
        </div>
      ))}
    </div>
  );
}

export default Shastars;
