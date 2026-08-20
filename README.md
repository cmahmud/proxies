# SyndProxy private pool

## Current pool

- Alive now: 1522
- Gold now: 553
- HTTP: 604 alive / 179 gold
- HTTPS: 445 alive / 88 gold
- SOCKS4: 229 alive / 127 gold
- SOCKS5: 244 alive / 159 gold

## Historical pool

- Discovered: 138813
- Ever alive: 23019
- Ever gold: 911

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
