# SyndProxy private pool

## Current pool

- Alive now: 1177
- Gold now: 497
- HTTP: 461 alive / 191 gold
- HTTPS: 305 alive / 114 gold
- SOCKS4: 203 alive / 81 gold
- SOCKS5: 208 alive / 111 gold

## Historical pool

- Discovered: 124849
- Ever alive: 19392
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
