import React, { useState } from 'react';
import './DataTable.css';

const DataTable = ({ data }) => {
  const [showAll, setShowAll] = useState(false);

  if (!data || data.length === 0) return null;

  const displayData = showAll ? data : data.slice(0, 10);
  const columns = Object.keys(data[0]);

  const exportToCSV = () => {
    const headers = columns.join(',');
    const rows = data.map(row => 
      columns.map(col => {
        const value = row[col];
        return typeof value === 'string' && value.includes(',') ? `"${value}"` : value;
      }).join(',')
    ).join('\n');
    
    const csv = `${headers}\n${rows}`;
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'real_estate_data.csv';
    a.click();
    window.URL.revokeObjectURL(url);
  };

  return (
    <div className="table-card">
      <div className="table-header">
        <h3>📋 Filtered Data</h3>
        <button onClick={exportToCSV} className="export-btn">
          💾 Export CSV
        </button>
      </div>
      
      <div className="table-container">
        <table className="data-table">
          <thead>
            <tr>
              {columns.map((col) => (
                <th key={col}>{col}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {displayData.map((row, index) => (
              <tr key={index}>
                {columns.map((col) => (
                  <td key={col}>
                    {col === 'Price' 
                      ? `₹${Number(row[col]).toLocaleString()}`
                      : row[col]}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      
      {data.length > 10 && (
        <div className="table-footer">
          <button
            onClick={() => setShowAll(!showAll)}
            className="toggle-btn"
          >
            {showAll ? '▲ Show Less' : `▼ Show All (${data.length} records)`}
          </button>
        </div>
      )}
    </div>
  );
};

export default DataTable;
