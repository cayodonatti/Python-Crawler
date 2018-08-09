const MongoClient = require("mongodb").MongoClient;
require("dotenv").config();

// Connection URL
const url = process.env.MONGO_STRING;

// Database Name
const dbName = "cifras";

const getDb = async () => {
  return await MongoClient.connect(url);
};

const main = async () => {
  let client = await getDb();
  if (!client) {
    console.log("Erro ao conectar ao servidor!");
    return;
  }

  const db = client.db(dbName);

  var lineReader = require("readline").createInterface({
    input: require("fs").createReadStream("../cifras_formatadas.json")
  });

  lineReader.on("line", async line => {
    if (line == "\n") return;

    let item = JSON.parse(line);

    let response = await db.collection("cifras").insertOne(item);
    console.log(response);

    while (response.insertedCount < 1) {
      response = await db.collection("cifras").insertOne(item);
      console.log(response);
    }
  });

  lineReader.on("close", async () => {
    await client.close();
    process.exit();
  });
};

main().then(() => {});
