# SyndProxy private pool

## Current pool

- Alive now: 963
- Gold now: 369
- HTTP: 288 alive / 63 gold
- HTTPS: 237 alive / 19 gold
- SOCKS4: 200 alive / 127 gold
- SOCKS5: 238 alive / 160 gold

## Historical pool

- Discovered: 110416
- Ever alive: 15720
- Ever gold: 502

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
