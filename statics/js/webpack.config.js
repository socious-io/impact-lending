const path = require("path");

module.exports = {
  mode: 'development',
  entry: "./main.js",
  output: {
    filename: "main.bundle.js",
    path: path.resolve(__dirname, "dist"),
  },
  devServer: {
    contentBase: path.join(__dirname, 'dist'),
    hot: true,  // enable HMR
    writeToDisk: true, // write files to disk
    // ...
  },
};
