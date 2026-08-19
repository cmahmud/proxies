# SyndProxy private pool

## Current pool

- Alive now: 906
- Gold now: 467
- HTTP: 285 alive / 124 gold
- HTTPS: 228 alive / 87 gold
- SOCKS4: 208 alive / 140 gold
- SOCKS5: 185 alive / 116 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17479
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
