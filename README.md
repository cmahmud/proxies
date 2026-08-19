# SyndProxy private pool

## Current pool

- Alive now: 1148
- Gold now: 502
- HTTP: 434 alive / 192 gold
- HTTPS: 314 alive / 115 gold
- SOCKS4: 198 alive / 81 gold
- SOCKS5: 202 alive / 114 gold

## Historical pool

- Discovered: 124849
- Ever alive: 19392
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
