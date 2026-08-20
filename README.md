# SyndProxy private pool

## Current pool

- Alive now: 780
- Gold now: 379
- HTTP: 209 alive / 75 gold
- HTTPS: 151 alive / 17 gold
- SOCKS4: 204 alive / 146 gold
- SOCKS5: 216 alive / 141 gold

## Historical pool

- Discovered: 148336
- Ever alive: 26302
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
