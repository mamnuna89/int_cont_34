export default {
  __init__: ['customPaletteProvider'],
  customPaletteProvider: ['type', CustomPaletteProvider]
};

function CustomPaletteProvider(palette, create, elementFactory) {
  this._create = create;
  this._elementFactory = elementFactory;

  palette.registerProvider(this);
}

CustomPaletteProvider.$inject = ['palette', 'create', 'elementFactory'];

CustomPaletteProvider.prototype.getPaletteEntries = function () {
  const { _create, _elementFactory } = this;

  function createShape(type) {
    return function (event) {
      const shape = _elementFactory.createShape({ type });
      _create.start(event, shape);
    };
  }

 
  return {
  'create.start-event': {
    group: 'event',
    className: 'entry bpmn-icon-start-event-none',
    title: 'Старт',
    action: {
      dragstart: createShape('bpmn:StartEvent'),
      click: createShape('bpmn:StartEvent')
    }
  },
  'create.task': {
    group: 'activity',
    className: 'entry bpmn-icon-task',
    title: 'Задача',
    action: {
      dragstart: createShape('bpmn:Task'),
      click: createShape('bpmn:Task')
    }
  },
  'create.gateway': {
    group: 'gateway',
    className: 'entry bpmn-icon-gateway-xor',
    title: 'Шлюз',
    action: {
      dragstart: createShape('bpmn:ExclusiveGateway'),
      click: createShape('bpmn:ExclusiveGateway')
    }
  }
};
