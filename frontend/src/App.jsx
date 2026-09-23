import { useState, useEffect } from 'react'
import { fetchHealthStatus } from './services/api'
import './App.css'

function App() {
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  const checkBackend = async () => {
    setLoading(true)
    setError(null)
    try {
      const result = await fetchHealthStatus()
      setData(result)
    } catch (err) {
      setError(err.message || 'Failed to connect to backend')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    checkBackend()
  }, [])

  return (
    <div className="container">
      <header className="header">
        <h1>CYBERHUB</h1>
        <p className="subtitle">AI-Powered Public Digital Identity Intelligence System</p>
      </header>

      <main className="card">
        <h2>Backend Connection Status</h2>

        {loading && (
          <div className="status-box loading">
            <p>🔄 Connecting to FastAPI backend...</p>
          </div>
        )}

        {error && (
          <div className="status-box error">
            <p className="status-title">❌ Connection Error</p>
            <p className="status-detail">{error}</p>
            <button onClick={checkBackend} className="retry-btn">
              Retry Connection
            </button>
          </div>
        )}

        {data && (
          <div className="status-box success">
            <p className="status-title">✅ Connected to Backend</p>
            <div className="status-info">
              <p><strong>Status:</strong> <span className="badge">{data.status}</span></p>
              <p><strong>Message:</strong> {data.message}</p>
            </div>
            <button onClick={checkBackend} className="refresh-btn">
              Refresh Status
            </button>
          </div>
        )}
      </main>

      <footer className="footer">
        <p>CyberHub Foundation - Step 2 Integration Complete</p>
      </footer>
    </div>
  )
}

export default App
