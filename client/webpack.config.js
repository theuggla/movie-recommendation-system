/**
 * Webpack configs.
 */

// Imports
let path = require('path')

// Config
module.exports = {
  entry: [
    './src/index.jsx'
  ],
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      }
    ]
  },
  output: {
    path: path.resolve(__dirname, 'static'),
    filename: 'bundle.js'
  }
}
