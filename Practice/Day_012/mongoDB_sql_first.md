```sql
// create python db

use python_db;

//create people collection
db.createCollection('people')

//isCapped()
db.people.isCapped()

//collection statis information
db.people.stats()

//emp collection create and drop
db.createCollection('emp')
// Rename emp -> employees
//db.emp.renameCollection('employees')
db.emp.drop()

// Insert one document(row)
db.people.insertOne({
    user_id : 'bcd001',
    age : 45,
    status : 'A',
})

db.people.find()
db.people.find({})

// select _id, user_id, age from people
db.people.find(
{}, // where
{user_id :1, age: 1} // select
) //

db.people.find(
{},{user_id:1, status : 1, _id: 0} // 1 or 0
)

// insertMany : insert multiple document
db.people.insertMany([
    { user_id: "bcd002", age:25,status:"B" },
    { user_id: "bcd003", age:50,status:"A" },
    { user_id: "bcd004", age:35,status:"A" },
    { user_id: "abc001", age:28,status:"B" }
])
//SELECT * FROM people WHERE status = 'A'
db.people.find({ status: "A" })

//SELECT user_id,status from people where status = 'A'
db.people.find(
    { status: "A" },
    { user_id:1, status:1,_id:0}
    )

//SELECT * from people where status != 'A'
db.people.find(
    { status: { $ne:"A" }}
    )

//SELECT * FROM people WHERE status = 'A' AND age = 50
db.people.find(
    { status: "A", age: 50 }
    )

//SELECT status, user_id FROM people WHERE status = "A" OR age = 50
db.people.find(
    { $or: [ { status: "A" },{ age: 50 } ] },
    { user_id :1, status : 1, _id : 0}
    )

//SELECT age,user_id, status FROM people WHERE age > 30
db.people.find(
    { age : {$gt : 30}},
    { age : 1, user_id : 1, status :1}
)

//select user_id, status,age from people user_id !='abc001'
db.people.find(
    { user_id : {$ne : 'abc001'}},
    { user_id : 1, age : 1, status : 1}
)
//select * from people where age < 50 and age > 25
db.people.find(
    { age : {$gt : 25, $lt : 50}}
)

// status = 'C', user_id
db.people.insertOne(
    {status : 'C', user_id : 'abc006'}
    )


db.people.updateOne(
    { status :{ $eq : 'C'}}, // filter
    { $set : {user_id : 'abc007'}} // update action
)

//select * from people where age in (45,50)
db.people.find(
    { age : {$in : [45,50]}}
)

//select * from people where age not in (45,50)
db.people.find(
    { age : {$nin : [45,50]}}
)

//select * from people where user_id like '%bd%'
db.people.find(
    {user_id : {$regex : /bc/}}
)
//select * from people where user_id like 'bd%'
db.people.find(
    {user_id : {$regex : /^bc/}}
)

//select * from people where user_id like '%01'
db.people.find(
    {user_id : {$regex : /01$/}}
)

//select * from people status = 'A' order by user_id asc
db.people.find(
    {status : 'A'}
).sort({user_id:1})

//select user_id, age, status from people status = 'A' order by age desc
db.people.find(
    { status : 'A' },
    { user_id :1, age : 1, status : 1, _id :0 }
).sort({age : -1})

//select user_id, age from people where user_id like %cd% and age > 40
//order by user_id asc
db.people.find(
    {user_id : {$regex : /cd/}, age : { $gt : 40 } },
    { user_id : 1, age : 1, _id : 0 }
).sort({user_id : 1})

//select user_id, status, age from people where age >=25 and age <=45
// and status in ('A','B')
db.people.find(
    {age : {$gte : 25}, age : {$lte : 45}, status : {$in : ['A','B']} }
)

db.people.count({user_id : {$exists : true}})
db.people.find({user_id : {$exists : true}})

db.people.aggregate(
    [{$group : {_id : '$status' }}]
)

// update people set status = 'C' where age >= 45
db.people.updateMany(
    {age : {$gte : 45}},
    {$set : { status : 'C'}}
)
// update people set age = age + 10 where status = 'B'
db.people.updateMany(
    {status :'B'},
    {$inc : {age : 10}}
)
db.people.updateOne(
    {user_id : 'bcd001'},
    {$set : {age :100}}
)

// update people set age = age +7 where status = 'B'
db.people.updateOne(
    {status : 'B'},
    {$inc : {age :7}}
)
// delete from people where status = 'C'
db.people.deleteMany(
    {status : 'C'}
)

db.people.updateMany(
    {status : 'B'},
    {$set : {size : 1}} // formerly it doesn't exist 'size' attr,  
)                       // but can do that

db.people.find()
```