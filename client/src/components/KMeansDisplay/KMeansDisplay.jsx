/**
 * KMeansDisplay component
 */

import * as React from 'react'
import { Card, CardHeader, CardContent } from 'material-ui';

/**
 * Display class
 */
export class KMeansDisplay extends React.Component {
  /**
   * The render method
   */
  render () {
    const list = this.props.clusters;
    
    return this.props.visible ? (
      <div className='clusters'>
        { list.length > 0 ? list.map((item, index) => 
          <Card className='cluster'> 
            <CardHeader title={'Cluster #' + (index + 1)}/>
            <ul>
              {item.length > 0 ? item.map((blog) => <li>{blog}</li>) : <p>No blogs in this cluster</p>}
            </ul>
          </Card>
        ) : <p>Something went wrong with the clustering.</p> }
      </div>
    ) : ''
  }
}
