/**
 * App container
 */
import * as React from 'react'
import * as axios from 'axios'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'

import { ClusterDisplay } from '../../components/ClusterDisplay/ClusterDisplay.jsx'

/**
 * App class
 */
export class App extends React.Component {
  constructor (props) {
    super(props)
  }

  /**
   * componentDidMount
   */
  componentDidMount () {

  }

  /**
   * componentDidUpdate
   */
  componentDidUpdate (prevProps) {
    if (prevProps !== this.props) {

    }
  }

  /**
   * The render method
   */
  render () {
    return (
      <div className='app__wrapper'>
        <div className='app__sidebar' />
        <div className='app__content'>
          <Router>
            <Switch>
              <Route path='/' component={ClusterDisplay} />
            </Switch>
          </Router>
        </div>
      </div>
    )
  }
}
