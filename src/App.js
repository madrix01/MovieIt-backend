import React, { Component } from 'react';
import '.\App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Search from '.\Pages\Search';
import 'bootstrap\dist\css\bootstrap.css'
import PageNotFound from '.\Pages\PageNotFound';
class App extends Component{


  render(){
    
    return(
      <Router>
          <Switch>
            
          <Route exact path='/' component={Search} />
          <Route path='*' component={PageNotFound} />
          </Switch>
      </Router>
    );
    }
}

export default App;
