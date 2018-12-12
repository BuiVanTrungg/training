import React, { Component } from 'react';

import './css/Component.css';
import Table from './Table';
// import Demo from './Demo';

import Pagination from "react-js-pagination";
class Content extends Component {
	constructor(props) {
		super(props);
		this.state = {
			pageSize: '10',
			sdt: '',
			items: [],
			page: 1,
			errMess: '',
			isLoaded: false,
			isLoading: false,
		};
		// this.handleChange = this.handleChange.bind(this);
		// this.handleInput = this.handleInput.bind(this);
	}

	searchInput = React.createRef();

	componentDidMount() {
		this.getResult(this.state.page, this.state.pageSize, this.state.sdt);
	}
	handleChangePageSize = (event) => {
		this.setState({ pageSize: event.target.value });
		this.getResult(this.state.page, event.target.value, this.state.sdt);
	}
	
	handlePageChange = (event) => {
		this.setState({ page: event });
		this.getResult(event, this.state.pageSize, this.state.sdt);
	}

	handleInput = (e) => {
		clearTimeout(this.timeout);
		if (e.keyCode === 13) {
			this.getResult(this.state.page, this.state.pageSize, this.state.sdt);
		} else {
			this.setState({ sdt: this.searchInput.current.value }, () => {
				this.timeout = setTimeout(() => {
					this.getResult(this.state.page, this.state.pageSize, this.state.sdt);
				}, 1000);
			});
		}
	}

	getResult = (page, pageSize, sdt) => {
		this.setState({ isLoading: true });
		fetch(`http://localhost:5000/api/contacts?page=${page}&pageSize=${pageSize}&sdt=${sdt}`)
			.then(res => res.json())
			.then(json => {
				console.log(json)
				this.setState({
					isLoaded: true,
					items: json.data
				});
			})
			.catch(function (error) {
				// this.setState({ isLoaded: true, errMess: "ERROR"}); 
				console.log('Request failed', error);
			});
	}	
	render() {
		return (
			<div>
				<div className="input-pageSize">
					<div className="row">
						<div className="col-xs-6 col-sm-6 col-md-6 col-lg-6">
							<div className="get-page-size">
								<form>
									<select name="" id="input" className="form-control" onChange={this.handleChangePageSize} value={this.state.pageSize}>
										<option value="10">10</option>
										<option value="25">25</option>
										<option value="50">50</option>
										<option value="100">100</option>
									</select>
								</form>
								<p>&emsp;records per page</p>
							</div>
						</div>
						<div className="col-xs-6 col-sm-6 col-md-6 col-lg-6">
							<div className="search-box">
								<p>Search:&emsp;</p>
								<div className="input-group">
									<input type="text" onKeyUp={this.handleInput} ref={this.searchInput} />
								</div>
							</div>
						</div>
					</div>
				</div>
				<Table
					items={this.state.items}
					isLoaded={this.state.isLoaded}
					isLoading={this.state.isLoading}
					errMess={this.state.errMess}
				/>
				<div className="pagi">
					<Pagination
						activePage={this.state.page}
						itemsCountPerPage={this.state.pageSize}
						totalItemsCount={1500}
						pageRangeDisplayed={5}
						onChange={this.handlePageChange}
					/>
				</div>
			</div>

		);
	}
}

export default Content;
