import axios from "axios";

const api = axios.create({
  baseURL: "https://bluestock-6rhm.onrender.com/api/v1",
});

export default api;