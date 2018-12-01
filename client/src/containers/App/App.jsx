/**
 * App container
 */
import * as React from 'react'
import * as axios from 'axios'
import 'typeface-roboto'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'

import { SearchContainer } from '../SearchContainer/SearchContainer.jsx'

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
          <h1>Search Search</h1>
          <Router>
            <Switch>
              <Route path='/' component={SearchContainer} />
            </Switch>
          </Router>
        </div>
      </div>
    )
  }
}
