# SyndProxy private pool

## Current pool

- Alive now: 1061
- Gold now: 532
- HTTP: 356 alive / 157 gold
- HTTPS: 262 alive / 87 gold
- SOCKS4: 230 alive / 149 gold
- SOCKS5: 213 alive / 139 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18072
- Ever gold: 714

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
