# SyndProxy private pool

## Current pool

- Alive now: 809
- Gold now: 404
- HTTP: 219 alive / 81 gold
- HTTPS: 132 alive / 23 gold
- SOCKS4: 207 alive / 144 gold
- SOCKS5: 251 alive / 156 gold

## Historical pool

- Discovered: 155799
- Ever alive: 29344
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
