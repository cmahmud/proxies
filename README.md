# SyndProxy private pool

## Current pool

- Alive now: 1060
- Gold now: 405
- HTTP: 366 alive / 109 gold
- HTTPS: 258 alive / 23 gold
- SOCKS4: 217 alive / 150 gold
- SOCKS5: 219 alive / 123 gold

## Historical pool

- Discovered: 153722
- Ever alive: 28548
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
