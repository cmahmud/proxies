# SyndProxy private pool

## Current pool

- Alive now: 880
- Gold now: 377
- HTTP: 222 alive / 76 gold
- HTTPS: 243 alive / 18 gold
- SOCKS4: 200 alive / 147 gold
- SOCKS5: 215 alive / 136 gold

## Historical pool

- Discovered: 149510
- Ever alive: 26857
- Ever gold: 1088

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
