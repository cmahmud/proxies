# SyndProxy private pool

## Current pool

- Alive now: 734
- Gold now: 356
- HTTP: 195 alive / 68 gold
- HTTPS: 126 alive / 18 gold
- SOCKS4: 217 alive / 144 gold
- SOCKS5: 196 alive / 126 gold

## Historical pool

- Discovered: 145549
- Ever alive: 25398
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
