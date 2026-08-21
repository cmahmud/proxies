# SyndProxy private pool

## Current pool

- Alive now: 804
- Gold now: 408
- HTTP: 233 alive / 88 gold
- HTTPS: 149 alive / 22 gold
- SOCKS4: 194 alive / 142 gold
- SOCKS5: 228 alive / 156 gold

## Historical pool

- Discovered: 156414
- Ever alive: 29453
- Ever gold: 1127

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
