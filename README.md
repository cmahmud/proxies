# SyndProxy private pool

## Current pool

- Alive now: 1013
- Gold now: 398
- HTTP: 339 alive / 108 gold
- HTTPS: 245 alive / 22 gold
- SOCKS4: 207 alive / 145 gold
- SOCKS5: 222 alive / 123 gold

## Historical pool

- Discovered: 153186
- Ever alive: 28509
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
