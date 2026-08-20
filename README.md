# SyndProxy private pool

## Current pool

- Alive now: 811
- Gold now: 397
- HTTP: 216 alive / 77 gold
- HTTPS: 158 alive / 22 gold
- SOCKS4: 233 alive / 150 gold
- SOCKS5: 204 alive / 148 gold

## Historical pool

- Discovered: 150519
- Ever alive: 27049
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
