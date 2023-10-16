import React, { useState } from 'react';

function OrderForm() {
  const [formData, setFormData] = useState({
    user_id: '',
    pizza_id: '',
    quantity: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('/orders', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
       
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>User ID:</label>
        <input
          type="number"
          name="user_id"
          value={formData.user_id}
          onChange={handleChange}
        />
      </div>
      <div>
        <label>Pizza ID:</label>
        <input
          type="number"
          name="pizza_id"
          value={formData.pizza_id}
          onChange={handleChange}
        />
      </div>
      <div>
        <label>Quantity:</label>
        <input
          type="number"
          name="quantity"
          value={formData.quantity}
          onChange={handleChange}
        />
      </div>
      <button type="submit">Create Order</button>
    </form>
  );
}

export default OrderForm;