# SyndProxy private pool

## Current pool

- Alive now: 1001
- Gold now: 529
- HTTP: 342 alive / 154 gold
- HTTPS: 239 alive / 86 gold
- SOCKS4: 218 alive / 150 gold
- SOCKS5: 202 alive / 139 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18041
- Ever gold: 713

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
