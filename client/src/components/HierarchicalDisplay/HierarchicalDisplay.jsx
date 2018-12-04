/**
 * HierarchicalDisplay component
 */

import * as React from 'react'

/**
 * Dsplay class
 */
export class HierarchicalDisplay extends React.Component {
  /**
   * The render method
   */
  render () {

    return this.props.visible ? (
        <div className='cluster'>
          <img src={this.props.src} />
        </div>
    ) : ''
  }
}
