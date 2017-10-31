# insightPy
./bd.py>starts webserver at localost:5000
/templates> dynamic html dir
/static> css,js files
/mongod utils:
    ./mongo db.pene2.test.find()                    -- lists all elements in the collection 'test' of db 'pene2'
            db.pene2.insertOne({"name": "Succubus") -- inserts Succubus to db
            db.pene2.delete_many({})                --  remove all elements from collection
    ***     
    ./mongod --dbpath ~/insightPy/db --smallfiles   -- set path to db

    save db in /data/db>
