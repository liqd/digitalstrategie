const webpack = require('webpack')
const path = require('path')
const glob = require('glob')
const CopyWebpackPlugin = require('copy-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')

module.exports = {
  entry: {
    digitalstrategie: [
      './digitalstrategie/assets/scss/style.scss',
    ]
  },
  output: {
    // exposes exports of entry points
    library: {
      name: '[name]',
      // return value of entry point will be assigned this.
      type: 'this'
    },
    // creates a folder to store all assets
    path: path.resolve('./digitalstrategie/static/'),
    // location they can be accessed, can also be a url
    publicPath: '/static/'
  },
  externals: {
    django: 'django'
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules\/(?!(bootstrap)\/).*/, // exclude all dependencies but bootstrap
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'].map(require.resolve),
          }
        }
      },
      {
        test: /\.s?css$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader
          },
          {
            loader: 'css-loader'
          },
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: [
                  require('autoprefixer')
                ]
              }
            }
          },
          {
            loader: 'sass-loader'
          }
        ]
      },
      {
        test: /(fonts|files)\/.*\.(svg|woff2?|ttf|eot|otf)(\?.*)?$/,
        // defines asset should always have seperate file
        type: 'asset/resource',
        generator: {
          // defines custom location of those files
          filename: 'fonts/[name][ext]'
        }
      },
      {
        test: /\.svg$|\.png$/,
        type: 'asset/resource',
        generator: {
          filename: 'images/[name][ext]'
        }
      }
    ]
  },
  resolve: {
    // redirect module requests when normal resolving fails.
    fallback: { path: require.resolve('path-browserify') },
    // attempt to resolve these extensions in this order.
    extensions: ['*', '.js', '.jsx', '.scss', '.css'],
    modules: [
      path.resolve('./node_modules')
    ].concat(
      glob.sync('./apps/*/assets/js').map(e => { return path.resolve(e) })
    )
  },
  plugins: [
    // extracts CSS into separate files
    new MiniCssExtractPlugin({
      filename: '[name].css',
      chunkFilename: '[id].css'
    }),
    // copies files or directories, to the build directory.
    new CopyWebpackPlugin({
      patterns: [{
        from: './digitalstrategie/assets/images/**/*',
        to: 'images/[name][ext]'
      }]
    })
  ]
}
