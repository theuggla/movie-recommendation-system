/**
 * AllUsersPage container
 */

import * as React from 'react'
import { User } from '../../components/User/User.jsx'

/**
 * AllUsersPage class
 */
export class AllUsersPage extends React.Component {
  constructor (props) {
    super(props)
    this.getUsers = this.getUsers.bind(this)
  }

  /**
   * The render method
   * */
  render () {
    const users = this.props.allUsers.map(this.getUsers).filter((user) => user !== undefined)

    return (
      <div className='users'>
        <h1 className='users__header'>Users</h1>
        <div className='users__wrapper'>
          {users}
        </div>
      </div>
    )
  }

  /**
   * Retrieves the desired user
   **/
  getUsers (user, i) {
    return <User key={i} user={user} />
  }
}
