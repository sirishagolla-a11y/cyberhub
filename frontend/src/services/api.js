const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

/**
 * Fetch health/root endpoint status from CyberHub FastAPI backend.
 */
export const fetchHealthStatus = async () => {
  const response = await fetch(`${API_URL}/`);
  if (!response.ok) {
    throw new Error(`Server error (${response.status})`);
  }
  return await response.json();
};
