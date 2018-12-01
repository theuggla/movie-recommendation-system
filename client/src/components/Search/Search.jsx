
/**
 * SearchDisplay component
 */

import * as React from 'react'
import { FlatButton as Button, TextField, Paper } from 'material-ui'
import { SearchResultDisplay } from '../SearchResultDisplay/SearchResultDisplay.jsx'

/**
 * Search class
 */
export class Search extends React.Component {
  /**
   * The render method
   */
  render () {
    return (
      <Paper className='search-display'>
      <h2>{this.props.header}</h2>
        <TextField
          floatingLabelText='Search query'
          onChange={this.props.handleChange('term-' + this.props.rank)}
        />
        <Button
          label='Search'
          onClick={() => {this.props.getSearchResults(this.props.rank, this.props.term).then((result) => this.props.handleChange('results-' + this.props.rank)(null, result.data))}}
        />
      { this.props.results && (this.props.results.length > 0 ? <Paper zDepth={2}>
        <SearchResultDisplay pages={this.props.results.length > 5 ? this.props.results.slice(0, 5) : this.props.results} />
      </Paper> : <p>No search results to show</p>)}
    </Paper>
    )
  }
}
