/**
 * Display component
 */

import * as React from 'react'
import { Card } from 'material-ui/Card'

/**
 * Doísplay class
 */
export class Display extends React.Component {
  /**
   * The render method
   */
  render () {
    const list = this.props.list

    return this.props.visible ? (
      <Card className='display'>
        <div className='list__content__information'>
          <ul>
            { list.length > 0 ? list.map((item) => <li> {item[1] + ': ' + item[0]} </li>) : <p>{this.props.message}</p> }
          </ul>
        </div>
      </Card>
    ) : ''
  }
}
