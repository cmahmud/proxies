# SyndProxy private pool

## Current pool

- Alive now: 1406
- Gold now: 566
- HTTP: 579 alive / 184 gold
- HTTPS: 366 alive / 89 gold
- SOCKS4: 220 alive / 132 gold
- SOCKS5: 241 alive / 161 gold

## Historical pool

- Discovered: 138835
- Ever alive: 23077
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
