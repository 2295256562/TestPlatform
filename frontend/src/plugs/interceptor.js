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
  axios.interceptors.response.use(response => {
    if (response.status === 200) {
      return Promise.resolve(response)
    }
  }, (err) => {
    if (err.response.status === 403) {
      localStorage.removeItem('token')
      location.href = '/#/login/'
    }
  })
}
export default MyHttpinterceptor
