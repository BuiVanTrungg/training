// contact controller

// import contact model

Contact = require('./contactModel');
// handle index
exports.index = function (req, res) {
    var page = parseInt(req.query.page) || 1;
    var pageSize = parseInt(req.query.pageSize) || 50;
    var sdt = req.query.sdt;
    var skip = (page - 1) * pageSize;

    if (sdt) {


        Contact.find({ link_fb: new RegExp(sdt, "i") })
            .skip(skip).limit(pageSize).exec((error, contact) => {
                if (error) {
                    console.log('Error');
                    res.json({
                        status: "error",
                        message: error,
                    })
                } else {
                    res.json({
                        status: "success",
                        message: "Contact retrieved successfully",
                        data: contact
                    })
                }
            })
    }
    else {


        // page*(pageSize+1)
        Contact.get(function (err, contact) {

            if (err) {
                res.json({
                    status: "error",
                    message: err,
                })
            }
            res.json({
                status: "success",
                message: "Contact retrieved successfully",
                data: contact
            })
        }, skip, pageSize)
    }
}

// handle create contact actions
exports.create = function (req, res) {
    console.log(req.body);
    const { name, link_fb, link_img, address, company } = req.body;
    // if (!name || !link_fb) {
    //     res.send(false);
    // }
    console.log("name", name);
    var contact = new Contact({
        name, link_fb, link_img, address, company
    });
    // contact.name = req.body && req.body.name ? req.body.name : contact.name;
    // contact.link_fb = req.body.link_fb;
    // contact.link_img = req.body.link_img;
    // contact.adress = req.body.address;
    // contact.company = req.body.company;
    // contact.email = req.body.email;
    // contact.phone = req.body.phone;
    // save the contact and check for errors
    contact.save(function (err) {
        if (err) {
            console.log(err);
            return res.status(500).send({ errors: { msg: err.message } });
        }
        return res.json({
            message: 'New contact created!',
            data: contact
        })
    })
}

// handle create contact actions
exports.view = function (req, res) {

    // Contact.find()
    //     .limit(pageSize)
    //     .exec(function(err, contact){
    //         Contact.count().exec(function(err, count) {
    //             res.render('contact', {
    //                 contact: contact,
    //                 page: page,
    //                 pages: count / pageSize
    //             })
    //         })
    //     })
    Contact.findById(req.params.contact_id, function (err, contact) {
        if (err)
            res.send(err);
        res.json({
            message: 'Contact details loading..',
            data: contact
        })
    })
}

// handle update contact info
exports.update = function (req, res) {
    Contact.findById(req.params.contact_id, function (err, contact) {
        if (err)
            return res.send(err);
        contact.name = req.body.name;
        contact.link_fb = req.body.link_fb;
        contact.link_img = req.body.link_img;
        contact.adress = req.body.address;
        contact.company = req.body.company;

        // save the contact and check for errors
        contact.save(function (err) {
            contact.save(function (err) {
                if (err)
                    return res.json(err);
                return res.json({
                    message: 'Contact Info updated',
                    data: contact
                })
            })
        })
    })
}

// handle delete contact
exports.delete = function (req, res) {
    Contact.remove({
        _id: req.params.contact_id
    }, function (err, contact) {
        if (err)
            res.send(err);
        res.json({
            status: "success",
            message: 'Contact deleted'
        })
    })
}