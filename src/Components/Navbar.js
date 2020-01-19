import React from 'react';
import { Link, BrowserRouter } from 'react-router-dom';
const Navbar = ()=>{

    if(localStorage.getItem("token") && localStorage.getItem("token") === "true"){
        return(
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
      
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav mr-auto">
            <li className="nav-item active">
              <a className="nav-link waves-effect waves-light" href="#">Home <span className="sr-only">(current)</span></a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">Register</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">Login</a>
            </li>
            <li className="nav-item dropdown">
              <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Recommendations
              </a>
              <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                <a className="dropdown-item" href="#">Youtube</a>
                <a className="dropdown-item" href="#">Amazon Prime</a>
                <div className="dropdown-divider"></div>
                <a className="dropdown-item" href="#">Netflix</a>
              </div>
            </li>
          </ul>
          <form className="form-inline my-2 my-lg-0">
            
            <Link className="btn btn-danger my-2 my-sm-0" type="submit" to='/logout'>Logout</Link>
          </form>
        </div>
      </nav>
        );
    }else{
        return(
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
      
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav mr-auto">
            <li className="nav-item active">
              <a className="nav-link" href="#">Home <span className="sr-only">(current)</span></a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">Register</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">Login</a>
            </li>
            <li className="nav-item dropdown">
              <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Recommendations
              </a>
              <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                <a className="dropdown-item" href="#">Youtube</a>
                <a className="dropdown-item" href="#">Amazon Prime</a>
                <div className="dropdown-divider"></div>
                <a className="dropdown-item" href="#">Netflix</a>
              </div>
            </li>
          </ul>
        </div>
      </nav>
        );
    }
}

export default Navbar