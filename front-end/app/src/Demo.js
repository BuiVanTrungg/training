import React, { Component } from 'react';

import './css/Component.css';
import Contact from './Contact';

class Demo extends Component {

	constructor(props) {
		super(props);
		this.state = {
			isLoaded: false,
			data: [],
		};
		this.onSortName = this.onSortName.bind(this);
	}

	onSortName(){
		this.setState({
			isSorted: true
		});
	}
	render() {

		var { isLoaded, items } = this.props;
		items = items ? Array.isArray(items) ? items : [items] : [];
		if (!isLoaded) {
			return <div>Loading....</div>
		}
		var ele = items.map((user, index) => {
				return <Contact key={user.link_fb}
					name={user.name}
					link_fb={user.link_fb}
					link_img={user.link_img}
					address={user.address}
					company={user.company}
				/>
			});
		// sort by name
		// if(this.state.isSorted){
		// 		var byName = items.slice(0);
		// 		byName.sort(function(a,b) {
		// 	    var x = a.name.toLowerCase();
		// 	    var y = b.name.toLowerCase();
		// 	    return x < y ? -1 : x > y ? 1 : 0;
		// 	});
		// 	var ele = byName.map((user, index) => {
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
			
		// }

		return (

			<div>
			test
			</div>
		);
	}
}

export default Demo;
