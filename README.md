# SyndProxy private pool

## Current pool

- Alive now: 864
- Gold now: 369
- HTTP: 296 alive / 81 gold
- HTTPS: 155 alive / 20 gold
- SOCKS4: 185 alive / 118 gold
- SOCKS5: 228 alive / 150 gold

## Historical pool

- Discovered: 166324
- Ever alive: 32392
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
