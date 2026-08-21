# SyndProxy private pool

## Current pool

- Alive now: 1003
- Gold now: 395
- HTTP: 305 alive / 89 gold
- HTTPS: 245 alive / 32 gold
- SOCKS4: 213 alive / 145 gold
- SOCKS5: 240 alive / 129 gold

## Historical pool

- Discovered: 160993
- Ever alive: 30910
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
