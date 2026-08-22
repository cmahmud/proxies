# SyndProxy private pool

## Current pool

- Alive now: 896
- Gold now: 401
- HTTP: 290 alive / 88 gold
- HTTPS: 166 alive / 27 gold
- SOCKS4: 217 alive / 150 gold
- SOCKS5: 223 alive / 136 gold

## Historical pool

- Discovered: 165824
- Ever alive: 32341
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
