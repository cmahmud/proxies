# SyndProxy private pool

## Current pool

- Alive now: 760
- Gold now: 397
- HTTP: 224 alive / 89 gold
- HTTPS: 120 alive / 27 gold
- SOCKS4: 183 alive / 123 gold
- SOCKS5: 233 alive / 158 gold

## Historical pool

- Discovered: 156424
- Ever alive: 29477
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
