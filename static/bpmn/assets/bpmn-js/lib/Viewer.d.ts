/**
 * A viewer for BPMN 2.0 diagrams.
 *
 * Have a look at {@link bpmn-js/lib/NavigatedViewer} or {@link bpmn-js/lib/Modeler} for bundles that include
 * additional features.
 *
 *
 * ## Extending the Viewer
 *
 * In order to extend the viewer pass extension modules to bootstrap via the
 * `additionalModules` option. An extension module is an object that exposes
 * named services.
 *
 * The following example depicts the integration of a simple
 * logging component that integrates with interaction events:
 *
 *
 * ```javascript
 *
 * // logging component
 * function InteractionLogger(eventBus) {
 *   eventBus.on('element.hover', function(event) {
 *     console.log()
 *   })
 * }
 *
 * InteractionLogger.$inject = [ 'eventBus' ]; // minification save
 *
 * // extension module
 * var extensionModule = {
 *   __init__: [ 'interactionLogger' ],
 *   interactionLogger: [ 'type', InteractionLogger ]
 * };
 *
 * // extend the viewer
 * var bpmnViewer = new Viewer({ additionalModules: [ extensionModule ] });
 * bpmnViewer.importXML(...);
 * ```
 *
 *
 * @extends BaseViewer<ServiceMap>
 *
 */
export default class Viewer<ServiceMap = null> extends BaseViewer<ServiceMap> {}

type BaseViewerOptions = import("./BaseViewer").BaseViewerOptions;
import BaseViewer from './BaseViewer';
