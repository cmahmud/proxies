# SyndProxy private pool

## Current pool

- Alive now: 1306
- Gold now: 386
- HTTP: 435 alive / 92 gold
- HTTPS: 323 alive / 17 gold
- SOCKS4: 265 alive / 137 gold
- SOCKS5: 283 alive / 140 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21576
- Ever gold: 885

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
