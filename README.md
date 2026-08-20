# SyndProxy private pool

## Current pool

- Alive now: 1205
- Gold now: 401
- HTTP: 414 alive / 102 gold
- HTTPS: 312 alive / 25 gold
- SOCKS4: 241 alive / 133 gold
- SOCKS5: 238 alive / 141 gold

## Historical pool

- Discovered: 144745
- Ever alive: 25145
- Ever gold: 1055

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
