import React from 'react';
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import './ChartDisplay.css';

const ChartDisplay = ({ chartData }) => {
  if (!chartData || !chartData.data) return null;

  const { type, data } = chartData;

  const renderPriceChart = () => {
    if (!data || data.length === 0) return null;

    return (
      <div className="chart-card">
        <h3>📈 Price Trend Analysis</h3>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis />
            <Tooltip formatter={(value) => `₹${value.toLocaleString()}`} />
            <Legend />
            <Line type="monotone" dataKey="price" stroke="#8b5cf6" strokeWidth={2} name="Price (₹)" />
          </LineChart>
        </ResponsiveContainer>
      </div>
    );
  };

  const renderDemandChart = () => {
    if (!data || data.length === 0) return null;

    return (
      <div className="chart-card">
        <h3>📊 Demand Trend Analysis</h3>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="demand" stroke="#10b981" strokeWidth={2} name="Demand Index" />
          </LineChart>
        </ResponsiveContainer>
      </div>
    );
  };

  const renderBothCharts = () => {
    const priceData = data.price || [];
    const demandData = data.demand || [];

    return (
      <>
        {priceData.length > 0 && (
          <div className="chart-card">
            <h3>📈 Price Trend</h3>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={priceData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="year" />
                <YAxis />
                <Tooltip formatter={(value) => `₹${value.toLocaleString()}`} />
                <Legend />
                <Line type="monotone" dataKey="price" stroke="#8b5cf6" strokeWidth={2} name="Price (₹)" />
              </LineChart>
            </ResponsiveContainer>
          </div>
        )}
        {demandData.length > 0 && (
          <div className="chart-card">
            <h3>📊 Demand Trend</h3>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={demandData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="year" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="demand" stroke="#10b981" strokeWidth={2} name="Demand" />
              </LineChart>
            </ResponsiveContainer>
          </div>
        )}
      </>
    );
  };

  const renderComparisonChart = () => {
    const priceData = data.price_data || [];
    const demandData = data.demand_data || [];

    return (
      <>
        {priceData.length > 0 && (
          <div className="chart-card">
            <h3>💰 Price Comparison</h3>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={priceData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="area" />
                <YAxis />
                <Tooltip formatter={(value) => `₹${value.toLocaleString()}`} />
                <Legend />
                <Bar dataKey="avg_price" fill="#8b5cf6" name="Avg Price (₹)" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        )}
        {demandData.length > 0 && (
          <div className="chart-card">
            <h3>📊 Demand Comparison</h3>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={demandData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="area" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="avg_demand" fill="#10b981" name="Avg Demand" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        )}
      </>
    );
  };

  switch (type) {
    case 'price':
      return renderPriceChart();
    case 'demand':
      return renderDemandChart();
    case 'both':
      return renderBothCharts();
    case 'comparison':
      return renderComparisonChart();
    default:
      return null;
  }
};

export default ChartDisplay;
