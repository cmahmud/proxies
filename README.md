# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 243
- HTTP: 439 alive / 33 gold
- HTTPS: 154 alive / 6 gold
- SOCKS4: 233 alive / 139 gold
- SOCKS5: 156 alive / 65 gold

## Historical pool

- Discovered: 102867
- Ever alive: 13643
- Ever gold: 426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
