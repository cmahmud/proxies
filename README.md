# SyndProxy private pool

## Current pool

- Alive now: 750
- Gold now: 379
- HTTP: 212 alive / 81 gold
- HTTPS: 138 alive / 21 gold
- SOCKS4: 194 alive / 129 gold
- SOCKS5: 206 alive / 148 gold

## Historical pool

- Discovered: 161996
- Ever alive: 31339
- Ever gold: 1157

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
