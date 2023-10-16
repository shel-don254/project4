import React from 'react';
import { Route, BrowserRouter as Router, NavLink, Routes } from 'react-router-dom';
import Form from './components/Form';
import UserList from './components/UserList';
import PizzaList from './components/PizzaList';
import ToppingList from './components/ToppingList';
import './App.css';

function App() {
  const backgroundStyle = {
    backgroundImage: `url('https://img.freepik.com/free-photo/close-up-delicious-pizza_23-2150852113.jpg?size=626&ext=jpg')`,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    height: '98vh',
    width: 'auto',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    textAlign: 'center',
    fontSize: '25px',
    fontFamily: 'Arial, Helvetica, sans-serif',
    fontStyle: 'italic',
    wordSpacing: '10px',
  };

  const navLinkStyle = {
    margin: '10px', 
  };

  const redTextStyle = {
    color: 'red', 
  };

  return (
    <div style={backgroundStyle}>
      <Router>
        <span className='logo' style={redTextStyle}> Welcome to the Pizza App </span>
        <nav>
          <NavLink to={`/form`} style={navLinkStyle}>Login</NavLink>
          <NavLink to={`/userlist`} style={navLinkStyle}>Profile</NavLink>
          <NavLink to={`/pizzalist`} style={navLinkStyle}>Pizzas</NavLink>
          <NavLink to={`/toppinglist`} style={navLinkStyle}>Toppings</NavLink>
        </nav>
        <Routes>
          <Route path="/form" element={<Form />} />
          <Route path="/userlist" element={<UserList />} />
          <Route path="/pizzalist" element={<PizzaList />} />
          <Route path="/toppinglist" element={<ToppingList />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
