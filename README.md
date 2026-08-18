# SyndProxy private pool

## Current pool

- Alive now: 651
- Gold now: 247
- HTTP: 174 alive / 31 gold
- HTTPS: 91 alive / 5 gold
- SOCKS4: 179 alive / 111 gold
- SOCKS5: 207 alive / 100 gold

## Historical pool

- Discovered: 95381
- Ever alive: 10238
- Ever gold: 377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
