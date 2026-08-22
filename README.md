# SyndProxy private pool

## Current pool

- Alive now: 729
- Gold now: 334
- HTTP: 228 alive / 90 gold
- HTTPS: 119 alive / 25 gold
- SOCKS4: 153 alive / 95 gold
- SOCKS5: 229 alive / 124 gold

## Historical pool

- Discovered: 167408
- Ever alive: 32568
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
