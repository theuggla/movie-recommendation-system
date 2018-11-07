/**
 * Specific routes for client application
 */
import * as React from 'react'
import { Route } from 'react-router-dom'

/**
 * Containers
 */
import { AllUsersPage } from '../containers/AllUsersPage/AllUsersPage.jsx'
import { UserPage } from '../containers/UserPage/UserPage.jsx'

/**
 * Routes to export
 */
export class ChildRoutes extends React.Component {
  render () {
    return (
      <div>
        <Route exact path='/' render={(props) => <AllUsersPage {...props} allUsers={this.props.allUsers} />} />
        <Route path='/user-:id' render={(props) => <UserPage {...props} allUsers={this.props.allUsers} />} />
      </div>
    )
  }
}
