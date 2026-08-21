# SyndProxy private pool

## Current pool

- Alive now: 756
- Gold now: 387
- HTTP: 228 alive / 85 gold
- HTTPS: 114 alive / 23 gold
- SOCKS4: 182 alive / 122 gold
- SOCKS5: 232 alive / 157 gold

## Historical pool

- Discovered: 156421
- Ever alive: 29474
- Ever gold: 1128

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
