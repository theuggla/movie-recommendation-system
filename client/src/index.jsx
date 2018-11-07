/**
 * Starting point of the app.
 */

// Imports
import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter as Router, Switch } from 'react-router-dom'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'

import './assets/styles.css'

import { MainRoutes as Routes } from './routes/MainRoutes.jsx'

// Render
ReactDOM.render(
  <MuiThemeProvider>
    <Router>
      <Switch>
        <Routes />
      </Switch>
    </Router>
  </MuiThemeProvider>, document.getElementById('app')
)
