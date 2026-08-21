# SyndProxy private pool

## Current pool

- Alive now: 1092
- Gold now: 415
- HTTP: 383 alive / 114 gold
- HTTPS: 257 alive / 27 gold
- SOCKS4: 238 alive / 151 gold
- SOCKS5: 214 alive / 123 gold

## Historical pool

- Discovered: 160027
- Ever alive: 30574
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
