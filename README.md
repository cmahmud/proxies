# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 362
- HTTP: 333 alive / 78 gold
- HTTPS: 218 alive / 22 gold
- SOCKS4: 210 alive / 124 gold
- SOCKS5: 228 alive / 138 gold

## Historical pool

- Discovered: 165812
- Ever alive: 32319
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
