# SyndProxy private pool

## Current pool

- Alive now: 1394
- Gold now: 408
- HTTP: 483 alive / 91 gold
- HTTPS: 327 alive / 18 gold
- SOCKS4: 260 alive / 149 gold
- SOCKS5: 324 alive / 150 gold

## Historical pool

- Discovered: 133965
- Ever alive: 21656
- Ever gold: 886

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
