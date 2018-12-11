/**
 * Starting point of the app.
 */

// Imports
import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter as Router, Route, Redirect, Switch } from 'react-router-dom'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'

import './assets/styles.css'

import { App } from './containers/App/App.jsx'
import { ErrorPage } from './containers/ErrorPage/ErrorPage.jsx'

// Render
ReactDOM.render(
  <MuiThemeProvider>
    <Router>
      <Switch>
        <Route exact path='/' render={(props) => <App {...props} />} />
        <Route path='/404' render={(props) => <ErrorPage {...props} />} />
        <Redirect from='*' to='/404' />
      </Switch>
    </Router>
  </MuiThemeProvider>, document.getElementById('app')
)
