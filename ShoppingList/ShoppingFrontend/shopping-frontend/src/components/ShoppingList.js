import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ShoppingList = () => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get('http://localhost:8000/api/items/');
      setItems(response.data);
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>Shopping List</h1>
      <ul>
        {items.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default ShoppingList;
