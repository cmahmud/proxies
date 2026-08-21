# SyndProxy private pool

## Current pool

- Alive now: 1088
- Gold now: 415
- HTTP: 380 alive / 115 gold
- HTTPS: 258 alive / 27 gold
- SOCKS4: 233 alive / 152 gold
- SOCKS5: 217 alive / 121 gold

## Historical pool

- Discovered: 160027
- Ever alive: 30572
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
