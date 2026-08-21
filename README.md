# SyndProxy private pool

## Current pool

- Alive now: 1023
- Gold now: 408
- HTTP: 349 alive / 102 gold
- HTTPS: 253 alive / 31 gold
- SOCKS4: 187 alive / 123 gold
- SOCKS5: 234 alive / 152 gold

## Historical pool

- Discovered: 152761
- Ever alive: 28358
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
