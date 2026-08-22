# SyndProxy private pool

## Current pool

- Alive now: 1030
- Gold now: 404
- HTTP: 300 alive / 92 gold
- HTTPS: 233 alive / 28 gold
- SOCKS4: 245 alive / 148 gold
- SOCKS5: 252 alive / 136 gold

## Historical pool

- Discovered: 161993
- Ever alive: 31314
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
