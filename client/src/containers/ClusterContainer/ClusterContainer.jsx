/**
 * ClusterContainer
 */
import * as React from 'react'

import { FlatButton as Button, DropDownMenu, MenuItem } from 'material-ui'
import * as axios from 'axios'

import { HierarchicalDisplay } from '../../components/HierarchicalDisplay/HierarchicalDisplay.jsx'
import { KMeansDisplay } from '../../components/KMeansDisplay/KMeansDisplay.jsx'

const iterations = [
  {
    value: '1',
    label: 'One iteration',
  },
  {
    value: '10',
    label: 'Ten iterations',
  },
  {
    value: '100',
    label: 'A hundread iterations',
  },
  {
    value: '1000',
    label: 'A thousand iterations',
  },
];

export class ClusterContainer extends React.Component {

  constructor (props) {
    super(props)

    this.state = {
      hierarchicalDisplay: false,
      hierarchical: false,
      kmeansDisplay: false,
      kmeans: false,
      kmeansiterativeDisplay: false,
      kmeansiterative: false,
      iterations: '10'
    }
  }

  /**
   * The render method
   */
  render () {
    return (
      <div className='display'>
        <h2>Hierarchical Clustering</h2>
          <Button 
            label="See Cluster"
            onClick={() => this.updateCluster('hierarchical', !this.state.hierarchicalDisplay)}
          />
          <HierarchicalDisplay src={this.state.hierarchical} visible={this.state.hierarchicalDisplay}/>

        <h2>K-means clustering</h2>
          <Button 
            label="Show clusters resulting from clustering until no reassignments are made" 
            onClick={() => {this.updateCluster('kmeans', !this.state.kmeansDisplay)}}
          />
          <KMeansDisplay clusters={this.state.kmeans} visible={this.state.kmeansDisplay}/>
          
          <div className="select-iterations">
            <Button 
              label="Show clusters with set number of iterations:" 
              onClick={() => {this.updateCluster('kmeans', !this.state.kmeansiterativeDisplay, this.state.iterations)}}
            />
            <DropDownMenu
              label="Iterations"
              value={this.state.iterations}
              onChange={(event, key, value) => {
                this.handleChange('iterations')(value)
                this.updateCluster('kmeans', true, this.state.iterations)
              }}
              underlineStyle={{display: 'none'}}
            >
              {iterations.map(option => (
                <MenuItem key={option.value} value={option.value} primaryText={option.label} />
              ))}
            </DropDownMenu>
          </div>
          <KMeansDisplay clusters={this.state.kmeansiterative} visible={this.state.kmeansiterativeDisplay}/>
      </div>
    )
  }

  /**
   * Handles change to state.
   */
  handleChange (name) {
    return (value) => {
      console.log('setting state ' + name + ' to ' + value)
      this.setState({
        [name]: value,
      });
    };
  }

  /**
   * Gets cluster data from the server and updates state.
   */
  updateCluster (clustername, visible, iterations) {
    this.getClusters(clustername, iterations).then((result) => {
      clustername = iterations ? clustername + 'iterative' : clustername
      this.handleChange(clustername)(result.data)
      this.handleChange(clustername + 'Display')(visible)
    })
  }

  /**
   * Retrieves result for clustering of the blogposts.
   */
  getClusters (type, iterations) {
    iterations = (type == 'kmeans') ? (iterations ? iterations : 'full') : ''
    return new Promise((resolve, reject) => {
      axios.get('http://127.0.0.1:5002/clusters/' + type + '/' + iterations)
      .then((result) => {
        resolve(result)
      })
    })
  }
}
