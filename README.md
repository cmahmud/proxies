# SyndProxy private pool

## Current pool

- Alive now: 1243
- Gold now: 423
- HTTP: 399 alive / 105 gold
- HTTPS: 319 alive / 31 gold
- SOCKS4: 206 alive / 124 gold
- SOCKS5: 319 alive / 163 gold

## Historical pool

- Discovered: 143501
- Ever alive: 24851
- Ever gold: 1050

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
