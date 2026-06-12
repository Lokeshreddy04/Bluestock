function KpiCards({ data }) {

  const latestProfit =
    data.profit_loss[
      data.profit_loss.length - 1
    ];

  const latestBalance =
    data.balance_sheet[
      data.balance_sheet.length - 1
    ];

  const latestCash =
    data.cash_flow[
      data.cash_flow.length - 1
    ];

  return (
    <div
      style={{
        display: "flex",
        gap: "20px",
        marginBottom: "20px"
      }}
    >
      <div>
        <h3>Revenue</h3>
        <p>{latestProfit.sales}</p>
      </div>

      <div>
        <h3>Net Profit</h3>
        <p>{latestProfit.net_profit}</p>
      </div>

      <div>
        <h3>Assets</h3>
        <p>{latestBalance.total_assets}</p>
      </div>

      <div>
        <h3>Free Cash Flow</h3>
        <p>{latestCash.free_cash_flow}</p>
      </div>
    </div>
  );
}

export default KpiCards;