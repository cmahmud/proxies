# SyndProxy private pool

## Current pool

- Alive now: 1184
- Gold now: 397
- HTTP: 395 alive / 101 gold
- HTTPS: 278 alive / 21 gold
- SOCKS4: 206 alive / 128 gold
- SOCKS5: 305 alive / 147 gold

## Historical pool

- Discovered: 136236
- Ever alive: 22562
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
