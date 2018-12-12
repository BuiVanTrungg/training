import React, { Component } from 'react';
// import logo from './logo.svg';
import './App.css';
import Header from './components/Header';
import Content from './components/Content';
import Demo from './components/Demo';
import {BrowserRouter, Route} from "react-router-dom"

class App extends Component {
  render() {
    return (

      <div>
      
      

      <div className="bg">
        <div>
          <Header />  
        </div>
        <div className="container bg-white">
          <BrowserRouter>
            <Route path="/contact" component={Content} />
          </BrowserRouter>
          <BrowserRouter>
            <Route path="/:name" component={Demo}/>
          </BrowserRouter>
        </div>
        <div className="container foot">
          <p>All right reserved. Data by <a href="/">timkh.com</a></p>
        </div>
        {/*<Sort />*/}
      </div>
      </div>
    );
  }
}

export default App;
