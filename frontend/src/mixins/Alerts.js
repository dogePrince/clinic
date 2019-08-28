class Alerts {
  constructor(){
    this.alerts_list = []
  }
  push(content, variant) {
    var this_vm = this;
    this.alerts_list.push({content: content, variant: variant, key: Math.random()});
    setTimeout(function(){ this_vm.alerts_list.shift() }, 3000);
  }
}

const alerts = new Alerts();
Object.freeze(alerts);

export default alerts;
