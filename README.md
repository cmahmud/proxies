# SyndProxy private pool

## Current pool

- Alive now: 668
- Gold now: 256
- HTTP: 172 alive / 33 gold
- HTTPS: 95 alive / 8 gold
- SOCKS4: 189 alive / 112 gold
- SOCKS5: 212 alive / 103 gold

## Historical pool

- Discovered: 95381
- Ever alive: 10238
- Ever gold: 377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
