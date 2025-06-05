function CustomPaletteProvider(palette, create, elementFactory, globalConnect) {
    this._create = create;
    this._elementFactory = elementFactory;
    this._globalConnect = globalConnect;

    palette.registerProvider(this);
}

CustomPaletteProvider.$inject = [
    'palette',
    'create',
    'elementFactory',
    'globalConnect'
];

CustomPaletteProvider.prototype.getPaletteEntries = function() {
    const { _create, _elementFactory } = this;

    function createTask() {
        return function(event) {
            const shape = _elementFactory.createShape({ type: 'bpmn:Task' });
            _create.start(event, shape);
        };
    }

    function createStartEvent() {
        return function(event) {
            const shape = _elementFactory.createShape({ type: 'bpmn:StartEvent' });
            _create.start(event, shape);
        };
    }

    function createExclusiveGateway() {
        return function(event) {
            const shape = _elementFactory.createShape({ type: 'bpmn:ExclusiveGateway' });
            _create.start(event, shape);
        };
    }

    return {
        'create.task': {
            group: 'activity',
            className: 'bpmn-icon-task',
            title: 'Создать задачу',
            action: {
                dragstart: createTask(),
                click: createTask()
            }
        },
        'create.start-event': {
            group: 'event',
            className: 'bpmn-icon-start-event-none',
            title: 'Создать стартовое событие',
            action: {
                dragstart: createStartEvent(),
                click: createStartEvent()
            }
        },
        'create.gateway': {
            group: 'gateway',
            className: 'bpmn-icon-gateway-xor',
            title: 'Создать шлюз',
            action: {
                dragstart: createExclusiveGateway(),
                click: createExclusiveGateway()
            }
        }
    };
};

export default {
    __init__: ['customPaletteProvider'],
    customPaletteProvider: ['type', CustomPaletteProvider]
};
