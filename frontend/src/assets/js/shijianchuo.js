// export function time(time = +new Date()) {
//     var date = new Date(time * 1000 + 8 * 3600 * 1000);
//     return date.toJSON().substr(0, 19).replace('T', ' ').replace(/-/g, '.');
// }

// export function time(nS)
//     {
//     return new Date(parseInt(nS) * 1000).toLocaleString().substr(0,17)
//     }
export function time(date){
    var date = new Date(date*1000);//如果date为13位不需要乘1000
    var Y = date.getFullYear() + '-';
    var M = (date.getMonth()+1 < 10 ? '0'+(date.getMonth()+1) : date.getMonth()+1) + '-';
    var D = (date.getDate() < 10 ? '0' + (date.getDate()) : date.getDate()) + ' ';
    var h = (date.getHours() < 10 ? '0' + date.getHours() : date.getHours()) + ':';
    var m = (date.getMinutes() <10 ? '0' + date.getMinutes() : date.getMinutes()) + ':';
    var s = (date.getSeconds() <10 ? '0' + date.getSeconds() : date.getSeconds());
    return Y+M+D+h+m+s;
}
