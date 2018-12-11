/**
 * App container
 */
import * as React from 'react'
import * as axios from 'axios'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'

import { ClusterContainer } from '../ClusterContainer/ClusterContainer.jsx'

/**
 * App class
 */
export class App extends React.Component {
  /**
   * The render method
   */
  render () {
    return (
      <div className='app__wrapper'>
        <div className='app__sidebar' />
        <div className='app__content'>
          <h1>Clustering</h1>
          <Router>
            <Switch>
              <Route path='/' component={ClusterContainer} />
            </Switch>
          </Router>
        </div>
      </div>
    )
  }
}
