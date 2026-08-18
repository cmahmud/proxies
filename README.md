# SyndProxy private pool

## Current pool

- Alive now: 1100
- Gold now: 281
- HTTP: 443 alive / 28 gold
- HTTPS: 178 alive / 4 gold
- SOCKS4: 246 alive / 136 gold
- SOCKS5: 233 alive / 113 gold

## Historical pool

- Discovered: 100097
- Ever alive: 12656
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
