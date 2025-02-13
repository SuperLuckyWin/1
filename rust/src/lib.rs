use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize)]
pub struct MarketData {
    pub timestamp: u64,
    pub price: f64,
    pub volume: f64,
}

#[derive(Serialize, Deserialize)]
pub enum Signal {
    Buy,
    Sell,
    Hold,
}

#[no_mangle]
pub extern "C" fn generate_signal(data: *const u8, len: usize) -> *const u8 {
    let market_data: MarketData = serde_json::from_slice(unsafe { std::slice::from_raw_parts(data, len) }).unwrap();
    let signal = if market_data.price > 100.0 {
        Signal::Buy
    } else {
        Signal::Sell
    };
    let signal_json = serde_json::to_string(&signal).unwrap();
    let signal_ptr = signal_json.as_ptr();
    std::mem::forget(signal_json); // Prevent Rust from freeing the memory
    signal_ptr
} 