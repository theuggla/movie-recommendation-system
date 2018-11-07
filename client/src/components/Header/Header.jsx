/**
 * Header component
 */
import * as React from 'react'
import { Paper, MenuItem } from 'material-ui'
import { Link } from 'react-router-dom'

/**
 * Header class
 */
export class Header extends React.Component {
  /**
  * The render method
  */
  render () {
    return (
      <Paper className='header'>
        <Link to='/' className='header__link'>
          <MenuItem>All users</MenuItem>
        </Link>
      </Paper>
    )
  }
}
