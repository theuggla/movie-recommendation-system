/**
 * Routes for client application
 */
import * as React from 'react'
import { Route, IndexRoute, Redirect } from 'react-router'

/**
 * Containers
 */
import { App } from '../containers/App/App'
import { AllUsersPage } from '../containers/AllUsersPage/AllUsersPage'
import { UserPage } from '../containers/UserPage/UserPage'
import { ErrorPage } from '../containers/ErrorPage/ErrorPage'

/**
 * Routes to export
 */
export default (
  <Route path='/' component={App}>
    <IndexRoute component={AllUsersPage} />
    <Route path='user-:id' component={UserPage} />
    <Route path='/404' component={ErrorPage} />
    <Redirect from='*' to='/404' />
  </Route>
)
