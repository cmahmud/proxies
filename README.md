# SyndProxy private pool

## Current pool

- Alive now: 1036
- Gold now: 525
- HTTP: 344 alive / 165 gold
- HTTPS: 285 alive / 90 gold
- SOCKS4: 189 alive / 124 gold
- SOCKS5: 218 alive / 146 gold

## Historical pool

- Discovered: 124835
- Ever alive: 19200
- Ever gold: 731

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
