/**
 * App container
 */
import * as React from 'react'
import * as axios from 'axios'
import { BrowserRouter as Router, Switch } from 'react-router-dom'

import { Header } from '../../components/Header/Header.jsx'
import { ChildRoutes as Routes } from '../../routes/ChildRoutes.jsx'

/**
 * App class
 */
export class App extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      users: []
    }
  }

  /**
   * componentDidMount
   * Retrieves the users.
   */
  componentDidMount () {
    axios.get('http://127.0.0.1:5002/users')
    .then((result) => {
      let users = result.data
      this.setState({ users })
    })
  }

  /**
   * componentDidUpdate
   * Updates the users on update.
   */
  componentDidUpdate (prevProps) {
    if (prevProps !== this.props) {
      axios.get('http://127.0.0.1:5002/users')
      .then((result) => {
        let users = result.data
        this.setState({ users })
      })
    }
  }

  /**
   * The render method
   */
  render () {
    return (
      <Router>
        <div className='app__wrapper'>
          <div className='app__sidebar'>
            <Header />
          </div>
          <div className='app__content'>
            <Switch>
              <Routes {...this.props} allUsers={this.state.users} />
            </Switch>
          </div>
        </div>
      </Router>
    )
  }
}
