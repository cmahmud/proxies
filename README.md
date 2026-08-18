# SyndProxy private pool

## Current pool

- Alive now: 1013
- Gold now: 324
- HTTP: 341 alive / 37 gold
- HTTPS: 228 alive / 10 gold
- SOCKS4: 212 alive / 149 gold
- SOCKS5: 232 alive / 128 gold

## Historical pool

- Discovered: 106889
- Ever alive: 14162
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
