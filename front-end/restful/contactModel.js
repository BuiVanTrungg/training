// contactModel.js

var mongoose = require('mongoose');

// Set up schema
var contactSchema = mongoose.Schema({
    // name: String,
    link_fb: String,
    link_img: String,
    address: String,
    company: String,
    name: {
        type: String,
        required : true
    },
    // email: {
    //     type: String,
    //     required : true
    // },
    // gender: String,
    // phone: String,
    // create_date:{
    //     type: String,
    //     default : Date.now
    // }
})

// Export contact model
var Contact = module.exports = mongoose.model('contact',contactSchema);

module.exports.get = function (callback,skip,limit){
    return Contact.find(callback).skip(skip).limit(limit);
}