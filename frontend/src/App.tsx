import { YMaps, Map, Placemark } from '@pbe/react-yandex-maps';
import { useState } from 'react';

export default function App() {
  const [additional, setAdditional] = useState(0);
  
  return (
    <YMaps>
      <div>
        <button style={{position: "absolute", zIndex: 20}} onClick={() => setAdditional(additional + 0.001)}>FLEX</button>
        <Map width={window.innerWidth} height={window.innerHeight} defaultState={{ center: [55.75, 37.57], zoom: 9 }}>
        <Placemark geometry={[55.75, 37.6]} properties={{hintContent: "Hint"}}/>
          <Placemark geometry={[55.75 + additional, 37.57]} options={{
            iconLayout: "default#image",
            iconImageSize: [128, 128],
            iconImageHref: "https://i.pinimg.com/originals/ed/88/35/ed8835d68bdb1c62f82a0f4dc51f020f.png"
          }}
          properties={{
            hintContent: "Frog Hype",
            balloonContent: "FROOOOOOOG"
          }}/>
        </Map>
      </div>
    </YMaps>
  )
}
