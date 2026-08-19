# SyndProxy private pool

## Current pool

- Alive now: 927
- Gold now: 462
- HTTP: 294 alive / 117 gold
- HTTPS: 221 alive / 88 gold
- SOCKS4: 218 alive / 140 gold
- SOCKS5: 194 alive / 117 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17486
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
