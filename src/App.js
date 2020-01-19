import React from 'react';
import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Switch, Route, Redirect } from 'react-router-dom';
import Navbar from './Components/Navbar';
import Register from './Pages/Register';
import Login from './Pages/Login';
import Home from './Pages/Home';
import Logout from './Pages/Logout';

function App() {
  return (
    <div className="App">
          <BrowserRouter>
          <Navbar />
            <Switch>
              <Route path='/home' component={Home} />
              <Route path='/register' component={Register} />
              <Route path='/login' component={Login} />
              <Route path='/logout' component={Logout} />
              
            </Switch>
          </BrowserRouter>
    </div>
  );
}

export default App;
