import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

function RevenueChart({ profitLoss }) {

  return (
    <LineChart
      width={800}
      height={400}
      data={profitLoss}
    >
      <CartesianGrid strokeDasharray="3 3" />

      <XAxis dataKey="year" />

      <YAxis />

      <Tooltip />

      <Line
        type="monotone"
        dataKey="net_profit"
      />
    </LineChart>
  );
}

export default RevenueChart;