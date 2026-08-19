# SyndProxy private pool

## Current pool

- Alive now: 1045
- Gold now: 469
- HTTP: 364 alive / 122 gold
- HTTPS: 283 alive / 85 gold
- SOCKS4: 212 alive / 142 gold
- SOCKS5: 186 alive / 120 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17468
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
