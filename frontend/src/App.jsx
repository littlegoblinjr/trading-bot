import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {
  Activity,
  Terminal,
  ArrowUpRight,
  RefreshCw,
  Zap,
  BarChart3,
  ShieldAlert
} from 'lucide-react';

const API_BASE = window.location.origin === 'http://localhost:5173'
  ? 'http://localhost:8000/api'
  : '/api';

function App() {
  const [symbol, setSymbol] = useState('BTCUSDT');
  const [side, setSide] = useState('BUY');
  const [typee, setTypee] = useState('MARKET');
  const [quantity, setQuantity] = useState('');
  const [price, setPrice] = useState('');
  const [stopPrice, setStopPrice] = useState('');
  const [logs, setLogs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState({ type: '', text: '' });

  useEffect(() => {
    const fetchLogs = async () => {
      try {
        const res = await axios.get(`${API_BASE}/logs`);
        setLogs(res.data.logs.reverse());
      } catch (err) {
        console.error("Log fetch failed", err);
      }
    };
    fetchLogs();
    const interval = setInterval(fetchLogs, 5000);
    return () => clearInterval(interval);
  }, []);

  const handleOrder = async (e) => {
    e.preventDefault();
    setLoading(true);
    setMessage({ type: '', text: '' });

    try {
      const res = await axios.post(`${API_BASE}/order`, {
        symbol,
        side,
        type: typee,
        quantity: parseFloat(quantity),
        price: price ? parseFloat(price) : null,
        stop_price: stopPrice ? parseFloat(stopPrice) : null,
      });
      setMessage({ type: 'success', text: `Order Placed: ID ${res.data.data.orderId}` });
    } catch (err) {
      setMessage({ type: 'error', text: err.response?.data?.detail || "Order failed" });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex bg-binance-bg min-h-screen text-gray-100 overflow-hidden">
      {/* Sidebar */}
      <aside className="w-64 border-r border-gray-800 bg-black/30 backdrop-blur-xl flex flex-col">
        <div className="p-6">
          <div className="flex items-center gap-2 mb-8">
            <div className="bg-binance-green/20 p-2 rounded-lg">
              <Zap className="text-binance-green w-6 h-6" />
            </div>
            <h1 className="text-xl font-bold tracking-tight">PRIMA<span className="text-binance-green">TRADE</span></h1>
          </div>

          <nav className="space-y-1">
            <button className="w-full flex items-center gap-3 px-4 py-3 bg-white/5 rounded-xl text-binance-green font-medium">
              <BarChart3 className="w-5 h-5" /> Dashboard
            </button>
          </nav>
        </div>

        <div className="mt-auto p-6">
          <div className="bg-white/5 rounded-2xl p-4 border border-white/10">
            <div className="flex items-center gap-2 mb-2 text-xs text-gray-500 uppercase tracking-widest font-bold">
              <Activity className="w-3 h-3 text-binance-green" /> System Status
            </div>
            <div className="text-sm font-semibold text-binance-green flex items-center gap-2">
              <div className="w-2 h-2 rounded-full bg-binance-green animate-pulse" />
              Binance Futures Live
            </div>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto p-8 relative">
        <div className="absolute top-0 right-0 w-96 h-96 bg-binance-green/5 blur-3xl rounded-full -translate-y-1/2 translate-x-1/2" />
        <div className="absolute bottom-0 left-0 w-96 h-96 bg-blue-500/5 blur-3xl rounded-full translate-y-1/2 -translate-x-1/2" />

        <header className="flex justify-between items-center mb-8 relative z-10">
          <div>
            <h2 className="text-3xl font-bold">Terminal Dashboard</h2>
            <p className="text-gray-400 text-sm mt-1">Manage and monitor your Binance Futures orders.</p>
          </div>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 relative z-10">
          <section className="lg:col-span-1">
            <div className="bg-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl p-6 shadow-2xl">
              <h3 className="text-lg font-bold mb-6 flex items-center gap-2">
                <Zap className="w-5 h-5 text-yellow-400" /> Quick Execution
              </h3>

              <form onSubmit={handleOrder} className="space-y-4">
                <div className="grid grid-cols-2 gap-2 p-1 bg-black/40 rounded-2xl border border-white/5">
                  <button
                    type="button"
                    onClick={() => setSide('BUY')}
                    className={`py-3 rounded-xl font-bold transition-all ${side === 'BUY' ? 'bg-binance-green text-black shadow-lg shadow-binance-green/20' : 'text-gray-500 hover:text-white'}`}
                  >
                    BUY
                  </button>
                  <button
                    type="button"
                    onClick={() => setSide('SELL')}
                    className={`py-3 rounded-xl font-bold transition-all ${side === 'SELL' ? 'bg-binance-red text-white shadow-lg shadow-binance-red/20' : 'text-gray-500 hover:text-white'}`}
                  >
                    SELL
                  </button>
                </div>

                <div className="space-y-1">
                  <label className="text-xs text-gray-500 font-bold uppercase ml-1">Symbol</label>
                  <input
                    className="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 outline-none focus:border-binance-green transition-all"
                    value={symbol}
                    onChange={(e) => setSymbol(e.target.value)}
                    placeholder="BTCUSDT"
                  />
                </div>

                <div className="space-y-1 relative">
                  <label className="text-xs text-gray-500 font-bold uppercase ml-1">Order Type</label>
                  <div className="grid grid-cols-3 gap-2">
                    {['MARKET', 'LIMIT', 'STOP'].map((t) => (
                      <button
                        key={t}
                        type="button"
                        onClick={() => setTypee(t)}
                        className={`py-2 text-[10px] font-bold rounded-lg border transition-all ${typee === t ? 'bg-binance-green/20 border-binance-green text-binance-green' : 'bg-white/5 border-white/10 text-gray-500 hover:border-white/20'}`}
                      >
                        {t}
                      </button>
                    ))}
                  </div>
                </div>

                <div className="space-y-1">
                  <label className="text-xs text-gray-500 font-bold uppercase ml-1">Quantity</label>
                  <div className="relative">
                    <input
                      className="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 outline-none focus:border-binance-green transition-all [appearance:textfield] [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none"
                      type="number"
                      step="any"
                      value={quantity}
                      onChange={(e) => setQuantity(e.target.value)}
                      placeholder="0.001"
                      required
                    />
                    <span className="absolute right-4 top-3.5 text-xs text-gray-500">UNIT</span>
                  </div>
                </div>

                {typee !== 'MARKET' && (
                  <div className="space-y-1 animate-in slide-in-from-top-2">
                    <label className="text-xs text-gray-500 font-bold uppercase ml-1">Limit Price</label>
                    <input
                      className="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 outline-none focus:border-binance-green transition-all [appearance:textfield] [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none"
                      type="number"
                      value={price}
                      onChange={(e) => setPrice(e.target.value)}
                      placeholder="95000.0"
                    />
                  </div>
                )}

                {typee === 'STOP' && (
                  <div className="space-y-1 animate-in slide-in-from-top-2">
                    <label className="text-xs text-gray-500 font-bold uppercase ml-1">Stop Price</label>
                    <input
                      className="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 outline-none focus:border-binance-green transition-all [appearance:textfield] [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none"
                      type="number"
                      value={stopPrice}
                      onChange={(e) => setStopPrice(e.target.value)}
                      placeholder="94500.0"
                    />
                  </div>
                )}

                <button
                  type="submit"
                  disabled={loading}
                  className="w-full bg-gradient-to-r from-binance-green to-blue-400 text-black font-black py-4 rounded-2xl mt-4 hover:scale-[1.02] active:scale-95 transition-all disabled:opacity-50 flex items-center justify-center gap-2"
                >
                  {loading ? <RefreshCw className="w-5 h-5 animate-spin" /> : <>PLACE {side} ORDER <ArrowUpRight className="w-5 h-5" /></>}
                </button>

                {message.text && (
                  <div className={`p-4 rounded-xl text-sm flex items-start gap-2 ${message.type === 'success' ? 'bg-binance-green/10 text-binance-green border border-binance-green/20' : 'bg-binance-red/10 text-binance-red border border-binance-red/20'}`}>
                    <ShieldAlert className="w-5 h-5 shrink-0" />
                    {message.text}
                  </div>
                )}
              </form>
            </div>
          </section>

          <section className="lg:col-span-2">
            <div className="bg-black/40 border border-white/10 rounded-3xl p-6 h-[600px] flex flex-col">
              <div className="flex justify-between items-center mb-6">
                <h3 className="text-lg font-bold flex items-center gap-2">
                  <Terminal className="w-5 h-5 text-binance-green" /> Trading Logs
                </h3>
                <span className="text-[10px] bg-white/5 px-2 py-1 rounded text-gray-500 uppercase">Live Feed</span>
              </div>

              <div className="flex-1 overflow-y-auto space-y-3 pr-2 scrollbar-thin">
                {logs.length > 0 ? logs.map((log, i) => (
                  <div key={i} className="text-xs font-mono py-2 border-b border-white/5 flex gap-4">
                    <span className="text-gray-600 shrink-0">{log.split(' - ')[0]}</span>
                    <span className={`shrink-0 font-bold ${log.includes('ERROR') ? 'text-binance-red' : 'text-binance-green'}`}>
                      {log.split(' - ')[1]}
                    </span>
                    <span className="text-gray-400 break-all">{log.split(' - ').slice(2).join(' - ')}</span>
                  </div>
                )) : (
                  <div className="h-full flex items-center justify-center text-gray-600 text-sm italic">
                    Waiting for log data...
                  </div>
                )}
              </div>
            </div>
          </section>
        </div>
      </main>
    </div>
  );
}

export default App;
