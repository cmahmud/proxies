# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 388
- HTTP: 124 alive / 53 gold
- HTTPS: 42 alive / 13 gold
- SOCKS4: 171 alive / 156 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33533
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
