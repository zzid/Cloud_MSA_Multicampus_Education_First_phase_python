```sql
use python_db;

db.createCollection('articles')

show collections

db.articles.insertMany([
    { "_id" : ObjectId("512bc95fe835e68f199c8686"), "author" : "john", "score" : 80, "views" : 100 },
    { "_id" : ObjectId("512bc962e835e68f199c8687"), "author" : "john", "score" : 85, "views" : 521 },
    { "_id" : ObjectId("55f5a192d4bede9ac365b257"), "author" : "ahn", "score" : 60, "views" : 1000 },
    { "_id" : ObjectId("55f5a192d4bede9ac365b258"), "author" : "li", "score" : 55, "views" : 5000 },
    { "_id" : ObjectId("55f5a1d3d4bede9ac365b259"), "author" : "annT", "score" : 60, "views" : 50 },
    { "_id" : ObjectId("55f5a1d3d4bede9ac365b25a"), "author" : "li", "score" : 94, "views" : 999 },
    { "_id" : ObjectId("55f5a1d3d4bede9ac365b25b"), "author" : "ty", "score" : 95, "views" : 1000 },
])

db.articles.find()

db.articles.aggregate(
    [ { $match : { author : "john" } } ]
);

db.articles.aggregate([
    {$match : { score : { $gte: 70 } } }
])

// author = 'li' and score > 60
db.articles.aggregate([
    {$match : {author : 'li', score : {$gte : 60}}}
])

// select author, sum(score) from aritcles group by author
db.articles.aggregate([
    {
        $group : {
            _id : '$author',
            total : {$sum : '$score'}
        }
    }
]);
// having
db.articles.aggregate([
    {
        $group : {
            _id : '$author',
            total : {$sum : '$score'}
        }
    },
    {
        $match : {
            total : {$gte : 100}
        }
    }
]);

db.createCollection('orders')
db.orders.deleteMany({})
db.orders.insertMany([
    {
      cust_id: "abc123",
      ord_date: ISODate("2012-01-02T17:04:11.102Z"),
      status: 'A',
      price: 100,
      items: [ { sku: "xxx", qty: 25, price: 1 },
               { sku: "yyy", qty: 25, price: 1 } ]
    },
    {
      cust_id: "abc123",
      ord_date: ISODate("2012-01-02T17:04:11.102Z"),
      status: 'A',
      price: 500,
      items: [ { sku: "xxx", qty: 25, price: 1 },
               { sku: "yyy", qty: 25, price: 1 } ]
    },
    {
      cust_id: "abc123",
      ord_date: ISODate("2012-01-02T17:04:11.102Z"),
      status: 'B',
      price: 130,
      items: [ { sku: "jkl", qty: 35, price: 2 },
               { sku: "abv", qty: 35, price: 1 } ]
    },
    {
      cust_id: "abc123",
      ord_date: ISODate("2012-01-02T17:04:11.102Z"),
      status: 'A',
      price: 130,
      items: [ { sku: "xxx", qty: 15, price: 1 },
               { sku: "yyy", qty: 15, price: 1 } ]
    },
    {
      cust_id: "abc123",
      ord_date: ISODate("2012-01-02T17:04:11.102Z"),
      status: 'B',
      price: 230,
      items: [ { sku: "jkl", qty: 35, price: 2 },
               { sku: "abv", qty: 35, price: 1 } ]
    },
    {
      cust_id: "abc456",
      ord_date: ISODate("2012-02-02T17:04:11.102Z"),
      status: 'C',
      price: 70,
      items: [ { sku: "jkl", qty: 45, price: 2 },
               { sku: "abv", qty: 45, price: 3 } ]
    },
    {
      cust_id: "abc456",
      ord_date: ISODate("2012-02-02T17:04:11.102Z"),
      status: 'A',
      price: 150,
      items: [ { sku: "xxx", qty: 35, price: 4 },
               { sku: "yyy", qty: 35, price: 5 } ]
    },
    {
      cust_id: "abc456",
      ord_date: ISODate("2012-02-02T17:04:11.102Z"),
      status: 'B',
      price: 20,
      items: [ { sku: "jkl", qty: 45, price: 2 },
               { sku: "abv", qty: 45, price: 1 } ]
    },
    {
      cust_id: "abc456",
      ord_date: ISODate("2012-02-02T17:04:11.102Z"),
      status: 'B',
      price: 120,
      items: [ { sku: "jkl", qty: 45, price: 2 },
               { sku: "abv", qty: 45, price: 1 } ]
    },
    {
      cust_id: "abc780",
      ord_date: ISODate("2012-02-02T17:04:11.102Z"),
      status: 'B',
      price: 260,
      items: [ { sku: "jkl", qty: 50, price: 2 },
               { sku: "abv", qty: 35, price: 1 } ]
    }
]);

db.orders.find()

// 1. select count(*) as count from orders
db.orders.aggregate([
    {
        $group : {
            _id : null,
            count : {$sum : 1}
        }
    }
])

// 2. select sum(price) as total from orders
db.orders.aggregate([
    {
        $group : {
            _id : null,
            total : {$sum : '$price'}
        }
    }
])

// select cust_id, sum(price) as total from orders group by cust_id
db.orders.aggregate([
    {
        $group : {
            _id : '$cust_id',
            total : {$sum : '$price'}
        }
    }
])

// + order by total asc
db.orders.aggregate([
    {
        $group : {
            _id : '$cust_id',
            total : {$sum : '$price'}
        }
    },
    {
        $sort : {total : 1}
    }
])

// select cust_id, ord_date, sum(price) as total from orders
// group by cust_id, ord_date

db.orders.aggregate([
    {
        $group :{
            _id : {
                cust_id : '$cust_id',
                ord_date : {
                    $dateToString : { format : "%Y-%m-%d", date : '$ord_date'}
                }
            },
            total : {$sum : '$price'}
        }
    }
])

// select cust_id, count(*) from orders group by cust_id
// having count(*) > 1
db.orders.aggregate([
    {
        $group : {
            _id : '$cust_id',
            count : {$sum : 1}
        }
    },
    {
        $match : {
            count : {$gt : 1}
        }
    }
])

// select status, count(*) from orders group by status
db.orders.aggregate([
    {
        $group : {
            _id : '$status',
            count : {$sum : 1}
        }
    }
])

// select status, sum(price) as total from orders group by status
db.orders.aggregate([
    {
        $group :{
            _id : '$status',
            total : {$sum : '$price'}
        }
    }
])


// select cust_id, ord_date, sum(price) as total from orders
// group by cust_id, ord_date
// having total > 290
db.orders.aggregate([
    {
        $group :{
            _id : {
                cust_id : '$cust_id',
                ord_date : {
                    $dateToString : { format : "%Y-%m-%d", date : '$ord_date'}
                }
            },
            total : {$sum : '$price'}
        }
    },
    {
        $match : {
            total : {$gt : 290}
        }
    }
])

// select cust_id, sum(price) as total from orders
// where status 'A'
// group by cust_id
db.orders.aggregate([
    {
        $match : {
            status : 'A'
        }
    },
    {
        $group : {
            _id : '$cust_id',
            total : {$sum : '$price'}
        }
    }
])

// select cust_id, ord_date, sum(price) as total from orders where status = 'B'
// group by cust_id, ord_date
db.orders.aggregate([
    {
        $match : {
            status : 'B'
        }
    },
    {
        $group : {
            _id : {
                cust_id : '$cust_id',
                ord_date : {
                    $dateToString : { format : "%Y-%m-%d", date : '$ord_date'}
                }
            },
            total : {$sum : '$price'}
        }
    }
])

// select cust_id, ord_date, sum(price) as total from orders where status = 'B'
// group by cust_id, ord_date
// having total > 250
db.orders.aggregate([
    {
        $match : {
            status : 'B'
        }
    },
    {
        $group : {
            _id : {
                cust_id : '$cust_id',
                ord_date : {
                    $dateToString : { format : "%Y-%m-%d", date : '$ord_date'}
                }
            },
            total : {$sum : '$price'}
        }
    },
    {
        $match : {
            total : {$gt : 250}
        }
    }
])

/*
select cust_id, sum(li.qty) as qty
from orders o, order_lineitem li
where o_id = li.order_id
group by cust_id
*/
db.orders.find()
db.orders.aggregate([
    {
        $unwind : '$items'
    },
    {
        $group : {
            _id : "$cust_id",
            qty : {$sum : '$items.qty'}
        }
    }
])


/*
    select count(*)
    from(
        select cust_id, ord_date
        from orders
        group by cust_id, ord_date
    )as d
*/

db.orders.find()
db.orders.aggregate([
    {
        $group :{
            _id : {
                cust_id : '$cust_id',
                ord_date : {
                    $dateToString : {
                        format : "%Y-%m-%d",
                        date : '$ord_date'
                    }
                }
            }
        }
    },
    {
        $group :{
            _id : null,
            count : {$sum : 1}
        }
    }
])




db.createCollection('items')
db.items.insertMany([
{ "_id" : 1, "item" : "abc", "price" : 10, "quantity" : 2, "date" : ISODate("2014-03-01T08:00:00Z") },
{ "_id" : 2, "item" : "jkl", "price" : 20, "quantity" : 1, "date" : ISODate("2014-03-01T09:00:00Z") },
{ "_id" : 3, "item" : "xyz", "price" : 5, "quantity" : 10, "date" : ISODate("2014-03-15T09:00:00Z") },
{ "_id" : 4, "item" : "xyz", "price" : 5, "quantity" : 20, "date" : ISODate("2014-04-04T11:21:39.736Z") },
{ "_id" : 5, "item" : "abc", "price" : 10, "quantity" : 10, "date" : ISODate("2014-04-04T21:23:13.331Z") },
])

db.items.find()

db.items.aggregate([
    {
        $group :{
            _id : {
                year : {$year : '$date'},
                month : {$month : '$date'},
                day : {$dayOfMonth : '$date'}
            },
            totalPrice : {
                $sum : {
                    $multiply : ['$price', '$quantity']
                }
            },
            avgCount : {
                $avg : '$quantity'
            },
            count : {$sum :1}
        }
    }
])

db.createCollection('inventory')
db.inventory.insertOne({ "_id" : 1, "item" : "ABC1", sizes: [ "S", "M", "L"] })
db.inventory.aggregate([
    {
        $unwind : "$sizes"
    }
])
```