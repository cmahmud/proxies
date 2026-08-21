# SyndProxy private pool

## Current pool

- Alive now: 762
- Gold now: 392
- HTTP: 233 alive / 91 gold
- HTTPS: 118 alive / 20 gold
- SOCKS4: 180 alive / 124 gold
- SOCKS5: 231 alive / 157 gold

## Historical pool

- Discovered: 156424
- Ever alive: 29484
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
