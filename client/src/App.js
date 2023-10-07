import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Form from './components/Form';
import UserList from './components/UserList';
import PizzaList from './components/PizzaList';
import ToppingList from './components/ToppingList';
import './App.css';

function App() {
  return (
    <div className='App'>
      <Router>
        <h1>Welcome to Bingo Pizza APP</h1>
        <Route path='/' exact>
          <video src='/video.mp4' controls autoPlay></video>
        </Route>
        <Route path='/users' component={UserList} />
        <Route path='/pizzas' component={PizzaList} />
        <Route path='/toppings' component={ToppingList} />
        <Route path='/orders' component={Form} />
      </Router>
    </div>
  );
}

export default App;
