# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 373
- HTTP: 337 alive / 69 gold
- HTTPS: 250 alive / 20 gold
- SOCKS4: 228 alive / 142 gold
- SOCKS5: 228 alive / 142 gold

## Historical pool

- Discovered: 113529
- Ever alive: 16388
- Ever gold: 516

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
