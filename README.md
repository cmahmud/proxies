# SyndProxy private pool

## Current pool

- Alive now: 1066
- Gold now: 360
- HTTP: 359 alive / 71 gold
- HTTPS: 245 alive / 12 gold
- SOCKS4: 213 alive / 130 gold
- SOCKS5: 249 alive / 147 gold

## Historical pool

- Discovered: 129290
- Ever alive: 20353
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
