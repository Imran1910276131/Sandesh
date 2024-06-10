/*eslint-disable*/
import React from 'react'

const Home = () => {
   
  return (
        <main role="main" className="container">
            <div className="row">
                <div className="col-md-8">
                    <h1>You can see all news after loging in </h1>
                </div>
                <div className="col-md-4">
                    <div className="content-section">
                        <h3>Our Sidebar</h3>
                        <p className='text-muted'>You can put any information here you'd like.
                                    <ul className="list-group">
                                <li className="list-group-item list-group-item-light">Latest Posts</li>
                                <li className="list-group-item list-group-item-light">Announcements</li>
                                <li className="list-group-item list-group-item-light">Calendars</li>
                                <li className="list-group-item list-group-item-light">etc</li>
                            </ul>
                        </p>
                    </div>
                </div>
            </div>
        </main>
  )
}

export default Home