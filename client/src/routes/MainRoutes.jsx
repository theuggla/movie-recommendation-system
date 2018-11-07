/**
 * Main routes for client application
 */
import * as React from 'react'
import { Route } from 'react-router-dom'

/**
 * Containers
 */
import { App } from '../containers/App/App.jsx'

/**
 * Routes to export
 */
export class MainRoutes extends React.Component {
  render () {
    return (
      <div>
        <Route path='/' render={(props) => <App {...props} />} />
      </div>
    )
  }
}
