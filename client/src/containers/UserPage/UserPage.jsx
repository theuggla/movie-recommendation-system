/**
 * UserPage container
 */
import * as React from 'react'
import { FlatButton as Button } from 'material-ui'
import * as axios from 'axios'

import { Display } from '../../components/Display/Display.jsx'

/**
 * UserPage class
 */
export class UserPage extends React.Component {
  constructor (props) {
    super(props)

    this.state = {
      user: false,
      euclidSimDisplay: false,
      euclidSims: false,
      pearsonSimDisplay: false,
      pearsonSim: false,
      euclidRecDisplay: false,
      euclidRecs: false,
      pearsonRecDisplay: false,
      pearsonRecs: false
    }
  }

  /**
   * Sets the correct user based on path
   */
  componentDidMount () {
    const userId = this.getCurrentUserId(this.props.location.pathname)
    this.setUser(this.props.allUsers, userId)
  }

  /**
   * Sets the correct user based on path on props update
   */
  componentDidUpdate (prevProps) {
    if (prevProps !== this.props) {
      const userId = this.getCurrentUserId(this.props.location.pathname)
      this.setUser(this.props.allUsers, userId)
    }
  }

  /**
   * The render method
   */
  render () {
    return this.state.user ? (
      <div className='user__wrapper'>
        <h1>{this.state.user['UserName']}</h1>
        <p>Ratings:</p>
        <ul>
          { this.state.user['Ratings'].map((rating) => <li> { rating['Movie'] + ': ' + rating['Rating'] } </li>) }
        </ul>
        <div className='sim euclid__sim'>
          <Button onClick={() => {
            this.getSim('euclid').then((result) => {
              this.setState({euclidSims: result.data})
              this.setState({ euclidSimDisplay: !this.state.euclidSimDisplay })
            })
          }}>
            <p>Similar users - euclid</p>
          </Button>
          <Display list={this.state.euclidSims} visible={this.state.euclidSimDisplay} message='No similar users in the database.' />
        </div>
        <div className='sim pearson__sim'>
          <Button onClick={() => {
            this.getSim('pearson').then((result) => {
              this.setState({pearsonSims: result.data})
              this.setState({ pearsonSimDisplay: !this.state.pearsonSimDisplay })
            })
          }}>
            <p>Similar users - pearson</p>
          </Button>
          <Display list={this.state.pearsonSims} visible={this.state.pearsonSimDisplay} message='No similar users in the database.' />
        </div>
        <div className='rec euclid__rec'>
          <Button onClick={() => {
            this.getRecs('euclid').then((result) => {
              this.setState({euclidRecs: result.data})
              this.setState({ euclidRecDisplay: !this.state.euclidRecDisplay })
            })
          }}>
            <p>Recommended movies - euclid</p>
          </Button>
          <Display list={this.state.euclidRecs} visible={this.state.euclidRecDisplay} message='This user have already seen all the movies in the world.' />
        </div>
        <div className='rec pearson__recs'>
          <Button onClick={() => {
            this.getRecs('pearson').then((result) => {
              this.setState({pearsonRecs: result.data})
              this.setState({ pearsonRecDisplay: !this.state.pearsonRecDisplay })
            })
          }}>
            <p>Recommended movies - pearson</p>
          </Button>
          <Display list={this.state.pearsonRecs} visible={this.state.pearsonRecDisplay} message='This user have already seen all the movies in the world.' />
        </div>
      </div>
    ) : <p>Wait</p>
  }

  /**
   * Retrieves a list of users similar to the
   * current user according to the given similarity measure
   */
  getSim (type) {
    return new Promise((resolve, reject) => {
      axios.get('http://127.0.0.1:5002/matches/' + type + '/' + this.state.user.UserID)
      .then((result) => {
        resolve(result)
      })
    })
  }

  /**
   * Retrieves a list of film recommendations for the
   * current user according to the given similarity measure
   */
  getRecs (type) {
    return new Promise((resolve, reject) => {
      axios.get('http://127.0.0.1:5002/recommendations/' + type + '/' + this.state.user.UserID)
      .then((result) => {
        resolve(result)
      })
    })
  }

  /**
   * Gets the current user ID
   */
  getCurrentUserId (pathname) {
    const id = pathname[0] === '/' ? pathname.slice(6) : pathname.slice(5)
    return id
  }

  /**
   * Sets the current user to state
   */
  setUser (users, id) {
    users.forEach((user) => {
      if (user.UserID === Number(id)) {
        this.setState({ user })
      }
    })
  }
}
