/*eslint-disable*/
import React from 'react'
import {Link} from 'react-router-dom'
const SingleNews = ({news}) => {
  return (
    <div className="media content-section">
          <img className="rounded-circle article-content" src="" alt="No Image" />
          <div className="media-body">
              <div className="article-metadata">
                  <Link className="mr-2" to="#">username</Link>
                  <small className="text-muted">{news.date}</small>
              </div>
              <h2><Link className="article-title" to="#" >{news.title}</Link></h2>
              <p className="article-content">{news.content}</p>
          </div>
    </div>
  )
}

export default SingleNews