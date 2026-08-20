# SyndProxy private pool

## Current pool

- Alive now: 1408
- Gold now: 527
- HTTP: 496 alive / 176 gold
- HTTPS: 365 alive / 60 gold
- SOCKS4: 212 alive / 124 gold
- SOCKS5: 335 alive / 167 gold

## Historical pool

- Discovered: 143501
- Ever alive: 24842
- Ever gold: 1050

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
