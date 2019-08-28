module.exports = {
  devServer: {
    host: 'localhost',
    proxy: {
      '/backend': {
        target: 'http://localhost:8000/backend',
        changeOrigin: true,
        ws: true,
        pathRewrite: {
          '^/backend': ''
        }
      }
    }
  }
}
