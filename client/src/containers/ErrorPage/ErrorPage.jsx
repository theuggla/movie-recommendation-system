/**
 * ErrorPage container
 */
import * as React from 'react'

/**
 * ErrorPage class
 */
export class ErrorPage extends React.Component {
  /**
   * The render method
   **/
  render () {
    return (
      <div className='users'>
        <h1 className='users__header users__header--error'>404 Not Found</h1>
        <p className='users__text'>Tyvärr, sidan du sökte verkar inte finnas.</p>
      </div>
    )
  }
}
