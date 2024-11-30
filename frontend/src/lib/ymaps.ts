import React from 'react';
import ReactDom from 'react-dom';

const [ymaps3React] = await Promise.all([ymaps3.import('@yandex/ymaps3-reactify'), ymaps3.ready]);

export const reactify = ymaps3React.reactify.bindTo(React, ReactDom);
export const {YMap, YMapDefaultSchemeLayer, YMapDefaultFeaturesLayer} = reactify.module(ymaps3);
// Import the package to add a default marker
ymaps3.import.registerCdn(
    'https://cdn.jsdelivr.net/npm/{package}',
    '@yandex/ymaps3-default-ui-theme@latest'
);

// @ts-ignore
export const {YMapHint, YMapHintContext} = reactify.module(await ymaps3.import('@yandex/ymaps3-hint@0.0.1'));
// @ts-ignore
export const {YMapDefaultMarker} = reactify.module(await ymaps3.import('@yandex/ymaps3-default-ui-theme'));