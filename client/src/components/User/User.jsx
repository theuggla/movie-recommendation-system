/**
 * User component
 */

import * as React from 'react'
import { Link } from 'react-router-dom'
import { Card, CardHeader } from 'material-ui/Card'

/**
 * User class
 */
export class User extends React.Component {
  /**
   * The render method
   */
  render () {
    const { user } = this.props

    return (
      <Card className='user'>
        <Link to={`user-${user.UserID}`} className='user__header'>
          <CardHeader
            title={user.UserName}
            classes={{ title: 'user__header__title' }}
          />
          <div className='user__content__information'>
            <p>Ratings:</p>
            <ul>
              { user['Ratings'].map((rating) => <li> { rating['Movie'] + ': ' + rating['Rating'] } </li>) }
            </ul>
          </div>
        </Link>
      </Card>
    )
  }
}
