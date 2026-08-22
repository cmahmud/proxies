# SyndProxy private pool

## Current pool

- Alive now: 1030
- Gold now: 366
- HTTP: 340 alive / 80 gold
- HTTPS: 261 alive / 22 gold
- SOCKS4: 217 alive / 136 gold
- SOCKS5: 212 alive / 128 gold

## Historical pool

- Discovered: 165836
- Ever alive: 32359
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
