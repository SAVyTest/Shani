import axios from "axios";
import { baseURL } from "../hooks/baseURL";

// const accessToken = localStorage.getItem("accessToken");
export const axiosClientForCapacity = axios.create({
  baseURL: baseURL + "/api",
  headers: { "Content-Type": "application/json" },
});

axiosClientForCapacity.interceptors.response.use(
  (res) => {
    return res;
  },
  async (err) => {
    const originalConfig = err.config;
    if (err.response) {
      if (err.response.status === 401) {
        if (window.localStorage.getItem("accessToken")) {
          localStorage.clear();
          window.location = window.location.origin + "/capacity-planner/login";
          return Promise.reject(err.response.data);
        }
      }
      if (err.response.status === 403 && err.response.data) {
        return Promise.reject(err.response.data);
      }
    }
    return Promise.reject(err);
  }
);
