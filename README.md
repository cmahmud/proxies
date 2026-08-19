# SyndProxy private pool

## Current pool

- Alive now: 1047
- Gold now: 496
- HTTP: 366 alive / 166 gold
- HTTPS: 242 alive / 46 gold
- SOCKS4: 227 alive / 140 gold
- SOCKS5: 212 alive / 144 gold

## Historical pool

- Discovered: 124833
- Ever alive: 19168
- Ever gold: 731

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
