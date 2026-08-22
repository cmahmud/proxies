# SyndProxy private pool

## Current pool

- Alive now: 991
- Gold now: 371
- HTTP: 338 alive / 90 gold
- HTTPS: 232 alive / 27 gold
- SOCKS4: 195 alive / 118 gold
- SOCKS5: 226 alive / 136 gold

## Historical pool

- Discovered: 165018
- Ever alive: 32268
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
