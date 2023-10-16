import React, { useEffect, useState } from 'react';

function PizzaList() {
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    fetch('/pizzas')
      .then((response) => response.json())
      .then((data) => setPizzas(data));
  }, []);

  return (
    <ul>
      {pizzas.map((pizza) => (
        <li key={pizza.id}>{pizza.name}</li>
      ))}
    </ul>
  );
}

export default PizzaList;