/**
 * ClusterContainer
 */
import * as React from 'react'

import { FlatButton as Button, TextField, Paper, Divider } from 'material-ui'
import { List } from 'material-ui/List'
import * as axios from 'axios'
import { SearchResultDisplay } from '../../components/SearchResultDisplay/SearchResultDisplay.jsx'

export class SearchContainer extends React.Component {

  constructor (props) {
    super(props)

    this.state = {
      term: '',
      results: []
    }
  }

  /**
   * The render method
   */
  render () {
    return (
      <div className='display'>
        <h2>Search FFS</h2>
          <TextField
            floatingLabelText='Search query'
            onChange={this.handleChange('term')}
            value={this.state.term}
          />
          <Button
            label='Search'
            onClick={() => {this.getSearchResults(this.state.term).then((result) => this.handleChange('results')(null, result.data))}}
          />
        <h2>Search Results</h2>
        { this.state.results.length > 0 && <Paper zDepth={2}>
          <SearchResultDisplay pages={this.state.results.length > 5 ? this.state.results.slice(0, 5) : this.state.results} />
        </Paper> }
      </div>
    )
  }

  /**
   * Handles change to state.
   */
  handleChange (name) {
    return (event, value) => {
      this.setState({
        [name]: value,
      });
    };
  }

  /**
   * Retrieves result for the search term.
   */
  getSearchResults (term) {
    return new Promise((resolve, reject) => {
      axios.get('http://127.0.0.1:5002/search/' + term)
      .then((result) => {
        resolve(result)
      })
    })
  }
}
