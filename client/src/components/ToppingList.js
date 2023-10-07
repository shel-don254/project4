import React, { useEffect, useState } from 'react';

function ToppingList() {
  const [toppings, setToppings] = useState([]);

  useEffect(() => {
    fetch('/toppings')
      .then((response) => response.json())
      .then((data) => setToppings(data));
  }, []);

  return (
    <ul>
      {toppings.map((topping) => (
        <li key={topping.id}>{topping.name}</li>
      ))}
    </ul>
  );
}

export default ToppingList;
