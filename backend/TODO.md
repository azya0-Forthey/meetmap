### Задачи для Никиты:

1. Вынести работу с токенами в отдельный сервис
2. Добавить активацию аккаунта по email
3. И много ещё чего...

### Задачи для Артёма:

1. ~~Допиить контейнер загрузки миграции~~
2. ~~Добавить географическую индексацию~~
3. ~~Протестировать~~
4. Добавить функцию ближайших точек
5. Переделать фронтенд

**Важно для тестов:**

```
SELECT name, position, ST_DistanceSphere(
  ST_GeomFromText('SRID=4326;POINT(30.458583 60.066742)'),
  position
) / 1000 AS distance
FROM placemarks
```

const getHint = useCallback((object) => object?.properties?.hint, []);
    const [placeMarks, setPlaceMarks] = useState([]);
    const {store} = useContext(Context);

    useEffect(() => {
        if (!store.isAuth) {
            return;
        }

        PLaceMarksService.getUserPlaceMarks(
        ).then(response => {setPlaceMarks(response.data)});
    });

    {/*@ts-ignore */}
            <YMapHint hint={getHint}>
                <HintWindow/>
            </YMapHint>


[
            {
                "zoom": 0,
                "color": "#9d6286",
                "scale": 0
            },
            {
                "zoom": 1,
                "color": "#9d6286",
                "scale": 0
            },
            {
                "zoom": 2,
                "color": "#9d6286",
                "scale": 0
            },
            {
                "zoom": 3,
                "color": "#9d6286",
                "scale": 0
            },
            {
                "zoom": 4,
                "color": "#9d6286",
                "scale": 0
            },
            {
                "zoom": 5,
                "color": "#9d6286",
                "scale": 0
            },
            {
                "zoom": 6,
                "color": "#9d6286",
                "scale": 2.64
            },
            {
                "zoom": 7,
                "color": "#9d6286",
                "scale": 2.84
            },
            {
                "zoom": 8,
                "color": "#9d6286",
                "scale": 3.13
            },
            {
                "zoom": 9,
                "color": "#9d6286",
                "scale": 3.55
            },
            {
                "zoom": 10,
                "color": "#9d6286",
                "scale": 3.21
            },
            {
                "zoom": 11,
                "color": "#9d6286",
                "scale": 2.72
            },
            {
                "zoom": 12,
                "color": "#9d6286",
                "scale": 2.35
            },
            {
                "zoom": 13,
                "color": "#9d6286",
                "scale": 2.02
            },
            {
                "zoom": 14,
                "color": "#9d6286",
                "scale": 1.81
            },
            {
                "zoom": 15,
                "color": "#9d6286",
                "scale": 1.69
            },
            {
                "zoom": 16,
                "color": "#9d6286",
                "scale": 1.66
            },
            {
                "zoom": 17,
                "color": "#9d6286",
                "scale": 1.31
            },
            {
                "zoom": 18,
                "color": "#9d6286",
                "scale": 1.08
            },
            {
                "zoom": 19,
                "color": "#9d6286",
                "scale": 0.93
            },
            {
                "zoom": 20,
                "color": "#9d6286",
                "scale": 0.84
            },
            {
                "zoom": 21,
                "color": "#9d6286",
                "scale": 0.8
            }
        ]