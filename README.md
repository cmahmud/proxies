# SyndProxy private pool

## Current pool

- Alive now: 747
- Gold now: 397
- HTTP: 220 alive / 89 gold
- HTTPS: 116 alive / 26 gold
- SOCKS4: 180 alive / 123 gold
- SOCKS5: 231 alive / 159 gold

## Historical pool

- Discovered: 156424
- Ever alive: 29477
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
