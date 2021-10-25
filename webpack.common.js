const webpack = require('webpack')
const path = require('path')
const glob = require('glob')
const CopyWebpackPlugin = require('copy-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')

module.exports = {
  entry: {
    digitalstrategie_external: [ // array of entry points
      './digitalstrategie/assets/external_css/berlin_marketing.css',
      './digitalstrategie/assets/external_css/swiper.min.css',
      './digitalstrategie/assets/external_css/shariff.min.css',
      'jquery',
      './digitalstrategie/assets/external_js/berlin_marketing.js',
      './digitalstrategie/assets/external_js/swiper.min.js',
      './digitalstrategie/assets/external_js/shariff.min.js',
      './digitalstrategie/assets/external_js/bo-foot-rebrush.js'
    ],
    digitalstrategie: [
      '@fortawesome/fontawesome-free/scss/fontawesome.scss',
      '@fortawesome/fontawesome-free/scss/brands.scss',
      '@fortawesome/fontawesome-free/scss/regular.scss',
      '@fortawesome/fontawesome-free/scss/solid.scss',
      './digitalstrategie/assets/scss/style.scss',
      './digitalstrategie/assets/js/app.js'
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
  // enables assets property for loading
  experiments: {
    asset: true
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules\/(?!(bootstrap)\/).*/, // exclude all dependencies but bootstrap
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react'].map(require.resolve),
            plugins: ['@babel/plugin-transform-runtime', '@babel/plugin-transform-modules-commonjs']
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
    // when using `npm link` for a4 dev env, dependencies are resolved against the linked
    // folder by default. This may result in dependencies being included twice.
    // Resolving against node_modules will prevent this.
    // concat merges node_modules and assets and syncs both to ensure no duplication.
    alias: {
      jquery$: 'jquery/dist/jquery.min.js'
    },
    modules: [
      path.resolve('./node_modules')
    ].concat(
      glob.sync('./apps/*/assets/js').map(e => { return path.resolve(e) })
    )
  },
  plugins: [
    // automatically load modules instead of import or require them everywhere.
    new webpack.ProvidePlugin({
      timeago: 'timeago.js', // do we need this?
      $: 'jquery',
      jQuery: 'jquery'
    }),
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
