db = new Mongo().getDB(process.env.MONGO_INITDB_DATABASE);

db.createCollection(process.env.PRODUCT_COLLECTION, { capped: false });