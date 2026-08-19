# SyndProxy private pool

## Current pool

- Alive now: 1059
- Gold now: 525
- HTTP: 364 alive / 163 gold
- HTTPS: 287 alive / 92 gold
- SOCKS4: 204 alive / 141 gold
- SOCKS5: 204 alive / 129 gold

## Historical pool

- Discovered: 119848
- Ever alive: 18421
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
