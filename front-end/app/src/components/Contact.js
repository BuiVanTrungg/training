import React, { Component } from 'react';

import './css/Component.css';

class Contact extends Component {

	render() {
		var test = this.props.link_fb.split("/")[3];
		return (
			<tr key = {this.props.link_fb}>
							<td data-table-header="Chủ nhà">
								<a href=" ">
									<img src={ this.props.link_img } alt="" className="avatar"/>
								</a>
							</td>
							<td data-table-header="Mã căn">
								<p>Tìm thông tin - facebook</p>
								<br/>
								<br/>
								<a href={test}>
									
									<span className="input-group-btn">
										<button type="button" className="btn btn-default color-but">Xem chi tiết</button>
									</span>
									
								</a>
							</td>
							<td data-table-header="Họ tên">
								{ this.props.name }
							</td>
							<td data-table-header="Địa chỉ">
								{ this.props.address }
							</td>
							<td data-table-header="Công ty">
								{ this.props.company }
							</td>
						</tr>
		);
	}
}

export default Contact;
