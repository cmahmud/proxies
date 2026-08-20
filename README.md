# SyndProxy private pool

## Current pool

- Alive now: 729
- Gold now: 365
- HTTP: 169 alive / 69 gold
- HTTPS: 149 alive / 18 gold
- SOCKS4: 213 alive / 138 gold
- SOCKS5: 198 alive / 140 gold

## Historical pool

- Discovered: 148336
- Ever alive: 26280
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
