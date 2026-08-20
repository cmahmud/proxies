# SyndProxy private pool

## Current pool

- Alive now: 1222
- Gold now: 404
- HTTP: 421 alive / 102 gold
- HTTPS: 309 alive / 28 gold
- SOCKS4: 239 alive / 134 gold
- SOCKS5: 253 alive / 140 gold

## Historical pool

- Discovered: 144741
- Ever alive: 25130
- Ever gold: 1055

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
