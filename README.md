# SyndProxy private pool

## Current pool

- Alive now: 1586
- Gold now: 648
- HTTP: 615 alive / 215 gold
- HTTPS: 491 alive / 109 gold
- SOCKS4: 234 alive / 156 gold
- SOCKS5: 246 alive / 168 gold

## Historical pool

- Discovered: 141223
- Ever alive: 23966
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
