# SyndProxy private pool

## Current pool

- Alive now: 1446
- Gold now: 563
- HTTP: 577 alive / 178 gold
- HTTPS: 395 alive / 90 gold
- SOCKS4: 228 alive / 133 gold
- SOCKS5: 246 alive / 162 gold

## Historical pool

- Discovered: 138827
- Ever alive: 23048
- Ever gold: 913

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
