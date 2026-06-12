import { formatNumber } from "../utils/formatters";

export const formatNumber = (
  value
) => {

  if (!value) {
    return "0";
  }

  return new Intl.NumberFormat(
    "en-IN",
    {
      maximumFractionDigits: 0,
    }
  ).format(value);

};
