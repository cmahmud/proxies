# SyndProxy private pool

## Current pool

- Alive now: 938
- Gold now: 405
- HTTP: 305 alive / 90 gold
- HTTPS: 184 alive / 29 gold
- SOCKS4: 224 alive / 150 gold
- SOCKS5: 225 alive / 136 gold

## Historical pool

- Discovered: 165824
- Ever alive: 32341
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
