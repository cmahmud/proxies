# SyndProxy private pool

## Current pool

- Alive now: 1490
- Gold now: 602
- HTTP: 628 alive / 198 gold
- HTTPS: 400 alive / 98 gold
- SOCKS4: 213 alive / 141 gold
- SOCKS5: 249 alive / 165 gold

## Historical pool

- Discovered: 138843
- Ever alive: 23106
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
