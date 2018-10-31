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
      <div className='error'>
        <h1 className='error__header'>404 Not Found</h1>
        <p className='error__text'>Tyvärr, sidan du sökte verkar inte finnas.</p>
      </div>
    )
  }
}
