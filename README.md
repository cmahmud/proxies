# SyndProxy private pool

## Current pool

- Alive now: 1061
- Gold now: 501
- HTTP: 351 alive / 139 gold
- HTTPS: 257 alive / 81 gold
- SOCKS4: 239 alive / 149 gold
- SOCKS5: 214 alive / 132 gold

## Historical pool

- Discovered: 119697
- Ever alive: 17905
- Ever gold: 705

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
