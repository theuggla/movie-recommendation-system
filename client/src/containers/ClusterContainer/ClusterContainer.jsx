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
      hierarchDisplay: false,
      hclustersrc: false,
      kmeansDisplayFull: false,
      kmeansclusterfull: false,
      kmeansDisplayItaration: false,
      kmeansclusteritative: false,
      iterations: '10'
    }
  }

  /**
   * The render method
   */
  render () {
    return (
      <div className='display'>
        <div className='hierarchical'>
        <h2>Hierarchical Clustering</h2>
          <Button label="See Cluster" onClick={() => {
            this.getHClust().then((result) => {
              this.setState({hclustersrc: result.data.link})
              this.setState({ hierarchDisplay: !this.state.hierarchDisplay })
            })
          }}>
          </Button>
          <HierarchicalDisplay src={this.state.hclustersrc} visible={this.state.hierarchDisplay}/>
        </div>
        <h2>K-means clustering</h2>
        <Button label="Show clusters resulting from clustering until no reassignments are made" onClick={() => {
            this.getKClust().then((result) => {
              this.setState({kmeansclusterfull: result.data})
              this.setState({ kmeansDisplayFull: !this.state.kmeansDisplayFull })
            })
          }}>
          </Button>
          <KMeansDisplay clusters={this.state.kmeansclusterfull} visible={this.state.kmeansDisplayFull}/>
          <div className="select-iterations">
          <Button className="iteration-button" label="Show clusters with set number of iterations:" onClick={() => {
                this.getKClust(this.state.iterations).then((result) => {
                  this.setState({kmeansclusteritative: result.data})
                  this.setState({ kmeansDisplayItaration: !this.state.kmeansDisplayItaration })
                })
              }}>
            </Button>
            <DropDownMenu
              label="Iterations"
              value={this.state.iterations}
              onChange={(event, key, value) => {
                this.handleChange('iterations')(value)
                this.getKClust(this.state.iterations).then((result) => {
                  this.setState({kmeansclusteritative: result.data})
                  this.setState({ kmeansDisplayItaration: true })
                })
              }}
              className="select-iterations-drop"
              underlineStyle={{display: 'none'}}
            >
              {iterations.map(option => (
                <MenuItem key={option.value} value={option.value} primaryText={option.label} />
              ))}
            </DropDownMenu>
          </div>
          <KMeansDisplay clusters={this.state.kmeansclusteritative} visible={this.state.kmeansDisplayItaration}/>
      </div>
    )
  }

  /**
   * Handles change to state.
   */
  handleChange (name) {
    return (value) => {
      this.setState({
        [name]: value,
      });
    };
  }

  /**
   * Retrieves a link to a hierarchical clustering of the blogposts.
   */
  getHClust () {
    return new Promise((resolve, reject) => {
      axios.get('http://127.0.0.1:5002/clusters/hierarchical')
      .then((result) => {
        resolve(result)
      })
    })
  }

  /**
   * Retrieves a list of k-means clustering of the blogposts.
   */
  getKClust (iterations) {
    return new Promise((resolve, reject) => {
      iterations = iterations ? iterations : 'full'
      axios.get('http://127.0.0.1:5002/clusters/kmeans/' + iterations)
      .then((result) => {
        resolve(result)
      })
    })
  }
}
