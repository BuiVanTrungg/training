import React, { Component } from 'react';
import {isEmpty} from 'lodash'

import './css/Component.css';

class Demo extends Component {
  constructor(props) {
    super(props);
    this.state = {
      item: {},
      more: [],
      errMess: '',
      isLoaded:false,
      rand :  1 + (Math.random() * (99)) 
    };
  }
  getResult(sdt, callback) {
    fetch(`http://localhost:5000/api/contacts?&sdt=${sdt}`)
      .then(res => res.json())
      .then(json => {
        console.log(json);
        const item = (json && json.data && json.data.length) ? json.data[0] : {};
        this.setState({
          isLoaded: true,
          item
        });

      })
      .catch(function (error) {
        console.log('Request failed', error);
      });
  }

  getTen(page) {
    fetch(`http://localhost:5000/api/contacts?&page=${page}&pageSize=10`)
      .then(res => res.json())
      .then(json => {
        console.log(json);
        this.setState({
          isLoaded: true,
          more: json.data
        });

      })
      .catch(function (error) {
        console.log('Request failed', error);
      });
  }
  componentWillMount(){
    this.getResult(this.props.match.params.name);
    this.getTen(this.state.rand);
  }
  render(){
    const { item } = this.state;
    var test=() =>{
        return <div>
        <p>test</p>

        </div>
      };
    return(
      <div>
      {
        !isEmpty(item) &&
        <div>
        <div className="user">
          <div className="img-user col-xs-3">
            <img src={item.link_img}/>
          </div>
          <div className="col-xs-9">
            <table className="table table-hover table-striped table-responsive">
            <thead>
              <tr>
                <th>Họ tên</th>
                <td>{item.name}</td>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th>SDT</th>
                <td>{this.props.match.params.name}</td>
              </tr>
              <tr>
                <th>Địa chỉ</th>
                <td>{item.address}</td>
              </tr>
              <tr>
                <th>Công ty</th>
                <td>{item.company}</td>
              </tr>
              <tr>
                <th>Facebook</th>
                <td>
                <a href={item.link_fb}>
                  <button type="button" className="btn btn-primary">Click</button>
                </a>
                </td>
              </tr>
            </tbody>
          </table>
          </div>
        </div>
        <hr />
        <button type="button" className="btn btn-default" disabled>
        <span>
          <i className="glyphicon glyphicon-eye-open"></i>
        </span>
        &emsp;Có thể bạn muốn xem
        </button>
        {this.test}
        <hr />
        <a href="/contact">
            <button type="button" className="btn btn-default btn-primary"> Home page</button>
          </a>
        </div>
      }
      </div>
    );
  }
}
export default Demo;