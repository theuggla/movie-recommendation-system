/**
 * Starting point of the app.
 */

// Imports
import React from 'react'
import ReactDOM from 'react-dom'
import { Router, browserHistory } from 'react-router'

import './assets/css/styles.css'
import routes from './routes/routes'

// Render
ReactDOM.render(
  <Router history={browserHistory} routes={routes} />, document.getElementById('app')
)
