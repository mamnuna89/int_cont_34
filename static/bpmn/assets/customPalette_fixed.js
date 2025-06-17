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
      html: '<div class="entry" title="Старт" style="font-family: bpmn-io-font; font-size: 22px;">&#xe845;</div>',
      action: {
        dragstart: createShape('bpmn:StartEvent'),
        click: createShape('bpmn:StartEvent')
      }
    },
    'create.end-event': {
      group: 'event',
      html: '<div class="entry" title="Финиш" style="font-family: bpmn-io-font; font-size: 22px;">&#xe84e;</div>',
      action: {
        dragstart: createShape('bpmn:EndEvent'),
        click: createShape('bpmn:EndEvent')
      }
    },
    'create.user-task': {
      group: 'activity',
      html: '<div class="entry" title="Задача пользователя" style="font-family: bpmn-io-font; font-size: 22px;">&#xe813;</div>',
      action: {
        dragstart: createShape('bpmn:UserTask'),
        click: createShape('bpmn:UserTask')
      }
    },
    'create.script-task': {
      group: 'activity',
      html: '<div class="entry" title="Скрипт-задача" style="font-family: bpmn-io-font; font-size: 22px;">&#xe81c;</div>',
      action: {
        dragstart: createShape('bpmn:ScriptTask'),
        click: createShape('bpmn:ScriptTask')
      }
    },
    'create.exclusive-gateway': {
      group: 'gateway',
      html: '<div class="entry" title="Исключающий шлюз" style="font-family: bpmn-io-font; font-size: 22px;">&#xe80f;</div>',
      action: {
        dragstart: createShape('bpmn:ExclusiveGateway'),
        click: createShape('bpmn:ExclusiveGateway')
      }
    },
    'create.parallel-gateway': {
      group: 'gateway',
      html: '<div class="entry" title="Параллельный шлюз" style="font-family: bpmn-io-font; font-size: 22px;">&#xe810;</div>',
      action: {
        dragstart: createShape('bpmn:ParallelGateway'),
        click: createShape('bpmn:ParallelGateway')
      }
    },
    'create.sub-process': {
      group: 'activity',
      html: '<div class="entry" title="Подпроцесс" style="font-family: bpmn-io-font; font-size: 22px;">&#xe81d;</div>',
      action: {
        dragstart: createShape('bpmn:SubProcess'),
        click: createShape('bpmn:SubProcess')
      }
    },
    'create.annotation': {
      group: 'artifact',
      html: '<div class="entry" title="Аннотация" style="font-family: bpmn-io-font; font-size: 22px;">&#xe82a;</div>',
      action: {
        dragstart: createShape('bpmn:TextAnnotation'),
        click: createShape('bpmn:TextAnnotation')
      }
    }
  };
};

window.customPaletteModule = {
  __init__: ['customPaletteProvider'],
  customPaletteProvider: ['type', CustomPaletteProvider]
};
