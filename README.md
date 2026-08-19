# SyndProxy private pool

## Current pool

- Alive now: 1052
- Gold now: 499
- HTTP: 349 alive / 139 gold
- HTTPS: 247 alive / 80 gold
- SOCKS4: 245 alive / 148 gold
- SOCKS5: 211 alive / 132 gold

## Historical pool

- Discovered: 119697
- Ever alive: 17906
- Ever gold: 705

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
