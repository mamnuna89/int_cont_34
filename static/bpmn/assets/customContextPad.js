function CustomContextPadProvider(contextPad, modeling) {
  this._modeling = modeling;
  contextPad.registerProvider(this);
}

CustomContextPadProvider.$inject = ['contextPad', 'modeling'];

CustomContextPadProvider.prototype.getContextPadEntries = function (element) {
  const modeling = this._modeling;

  return {
    delete: {
      group: 'edit',
      className: 'bpmn-icon-trash',
      title: 'Удалить элемент',
      action: {
        click: function () {
          modeling.removeElements([element]);
        }
      }
    }
  };
};

window.customContextPadModule = {
  __init__: ['customContextPadProvider'],
  customContextPadProvider: ['type', CustomContextPadProvider]
};
