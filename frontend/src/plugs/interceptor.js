import axios from "axios";

const MyHttpinterceptor = {}
MyHttpinterceptor.install = (Vue) => {
  axios.interceptors.request.use(config => {
    // 获取存在本地的token
    let token = localStorage.getItem('token')
    // 如果token存在那么就把token存到headers里
    if (token) {
      config.headers.Authorization = token
    }
    return config
  })
}
export default MyHttpinterceptor
