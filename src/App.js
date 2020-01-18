import React, { Component } from 'react';
import './App.css';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Search from './Pages/Search';
class App extends Component{

  constructor(props){
    super(props)
  }

  render(){
    return(
      <BrowserRouter>
         <Switch>
           <Route path='' Component={Search} />
         </Switch>
      </BrowserRouter>
    );
    }
}

export default App;
