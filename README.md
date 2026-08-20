# SyndProxy private pool

## Current pool

- Alive now: 1206
- Gold now: 403
- HTTP: 415 alive / 101 gold
- HTTPS: 307 alive / 28 gold
- SOCKS4: 239 alive / 134 gold
- SOCKS5: 245 alive / 140 gold

## Historical pool

- Discovered: 144745
- Ever alive: 25145
- Ever gold: 1055

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
