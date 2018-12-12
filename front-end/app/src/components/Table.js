import React, { Component } from 'react';

import './css/Component.css';
import Contact from './Contact';

class Table extends Component {

	constructor(props) {
		super(props);
		this.state = {
			isLoaded: false,
			data: [],
			isSorted: false,
			sort_asc: true
		};
		this.onSortName = this.onSortName.bind(this);
	}

	onSortName(){
		if (this.state.isSorted){
			this.setState({
				sort_asc : !this.state.sort_asc
			});
		}else{
			this.setState({
				isSorted : true
			});
		}

	}
	render() {
		// console.log(this.props)

		var { isLoaded, items } = this.props;
		items = items ? Array.isArray(items) ? items : [items] : [];
		if (!isLoaded) {
			return <div>Loading....</div>
		}

		// sort by name
		if(this.state.isSorted && this.state.sort_asc){
			var byName = items.slice(0);
			byName.sort(function(a,b) {
			    var x = a.name.toLowerCase();
			    var y = b.name.toLowerCase();
			    return x < y ? -1 : x > y ? 1 : 0;
			});
			var ele = byName.map((user, index) => {
				return <Contact key={user.link_fb}
					name={user.name}
					link_fb={user.link_fb}
					link_img={user.link_img}
					address={user.address}
					company={user.company}
				/>
			});
		}
		else if(this.state.isSorted){
			var byName = items.slice(0);
			byName.sort(function(a,b) {
			    var x = a.name.toLowerCase();
			    var y = b.name.toLowerCase();
			    return x > y ? -1 : x < y ? 1 : 0;
			});
			var ele = byName.map((user, index) => {
				return <Contact key={user.link_fb}
					name={user.name}
					link_fb={user.link_fb}
					link_img={user.link_img}
					address={user.address}
					company={user.company}
				/>
			});
		}
		else{
			var ele = items.map((user, index) => {
				return <Contact key={user.link_fb}
					name={user.name}
					link_fb={user.link_fb}
					link_img={user.link_img}
					address={user.address}
					company={user.company}
				/>
			});
		}

		// sort by address
		// if(this.state.isSorted && this.state.sort_asc){
		// 	var byAddress = items.slice(0);
		// 	byAddress.sort(function(a,b) {
		// 	    var x = a.address.toLowerCase();
		// 	    var y = b.address.toLowerCase();
		// 	    return x < y ? -1 : x > y ? 1 : 0;
		// 	});
		// 	var ele = byAddress.map((user, index) => {
		// 		return <Contact key={user.link_fb}
		// 			name={user.name}
		// 			link_fb={user.link_fb}
		// 			link_img={user.link_img}
		// 			address={user.address}
		// 			company={user.company}
		// 		/>
		// 	});
		// }
		// else if(this.state.isSorted){
		// 	var byAddress = items.slice(0);
		// 	byAddress.sort(function(a,b) {
		// 	    var x = a.address.toLowerCase();
		// 	    var y = b.address.toLowerCase();
		// 	    return x > y ? -1 : x < y ? 1 : 0;
		// 	});
		// 	var ele = byAddress.map((user, index) => {
		// 		return <Contact key={user.link_fb}
		// 			name={user.name}
		// 			link_fb={user.link_fb}
		// 			link_img={user.link_img}
		// 			address={user.address}
		// 			company={user.company}
		// 		/>
		// 	});
		// }
		// else{
		// 	var ele = items.map((user, index) => {
		// 		return <Contact key={user.link_fb}
		// 			name={user.name}
		// 			link_fb={user.link_fb}
		// 			link_img={user.link_img}
		// 			address={user.address}
		// 			company={user.company}
		// 		/>
		// 	});
		// }

		return (

			<div className="container">
				<table className="table table-hover table-striped ">
					<thead>
						<tr>
							<th className="">
							<i className="glyphicon glyphicon-sort-by-attributes"></i>
							Chủ nhà
							</th>
							<th className="">
							<i className="glyphicon glyphicon-sort-by-attributes"></i>
							Mã căn
							</th>
							<th className="">
							<span onClick={this.onSortName}>
								{
								this.state.sort_asc ? <i className="glyphicon glyphicon-sort-by-attributes"></i> : <i className="glyphicon glyphicon-sort-by-attributes-alt"></i>
								}
							</span>
							Họ tên
							</th>
							<th className="">
							<i className="glyphicon glyphicon-sort-by-attributes"></i>
							Địa chỉ
							</th>
							<th className="">
							<i className="glyphicon glyphicon-sort-by-attributes"></i>
							Công ty
							</th>
						</tr>
					</thead>
					<tbody>
						{ele}
					</tbody>
				</table>
			</div>
		);
	}
}

export default Table;
