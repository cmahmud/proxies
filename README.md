# SyndProxy private pool

## Current pool

- Alive now: 953
- Gold now: 404
- HTTP: 320 alive / 94 gold
- HTTPS: 180 alive / 25 gold
- SOCKS4: 236 alive / 149 gold
- SOCKS5: 217 alive / 136 gold

## Historical pool

- Discovered: 165824
- Ever alive: 32342
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
