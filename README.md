# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 542
- HTTP: 371 alive / 164 gold
- HTTPS: 249 alive / 93 gold
- SOCKS4: 208 alive / 145 gold
- SOCKS5: 206 alive / 140 gold

## Historical pool

- Discovered: 123169
- Ever alive: 18811
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
