# SyndProxy private pool

## Current pool

- Alive now: 1033
- Gold now: 245
- HTTP: 381 alive / 26 gold
- HTTPS: 241 alive / 2 gold
- SOCKS4: 204 alive / 122 gold
- SOCKS5: 207 alive / 95 gold

## Historical pool

- Discovered: 95391
- Ever alive: 10609
- Ever gold: 378

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
