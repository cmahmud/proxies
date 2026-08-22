# SyndProxy private pool

## Current pool

- Alive now: 983
- Gold now: 393
- HTTP: 305 alive / 88 gold
- HTTPS: 237 alive / 23 gold
- SOCKS4: 213 alive / 134 gold
- SOCKS5: 228 alive / 148 gold

## Historical pool

- Discovered: 164246
- Ever alive: 32084
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
