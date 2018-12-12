import React, { Component } from 'react';

class Header extends Component {
  render() {
    return (
      <div>
        <nav className="navbar navbar-inverse">
        	<div className="container-fluid">
        		<a className="navbar-brand" href = "/contact"><b>TIMKH.COM</b></a>
        	</div>
        </nav>
      </div>
    );
  }
}

export default Header;
