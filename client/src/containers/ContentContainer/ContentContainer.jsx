/**
 * Content container
 */
import * as React from 'react'

import { ClusterContainer } from '../ClusterContainer/ClusterContainer.jsx'

/**
 * Content container class
 */
export class ContentContainer extends React.Component {
  /**
   * The render method
   */
  render () {
    return (
      <div>
          <h2>Clustering with pre-defined word-list</h2>
          <ClusterContainer wordlist='initial' />
          <h2>Clustering with generated word-list</h2>
          <ClusterContainer wordlist='generated'/>
      </div>
    )
  }
}
