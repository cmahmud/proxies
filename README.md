# SyndProxy private pool

## Current pool

- Alive now: 1199
- Gold now: 534
- HTTP: 433 alive / 185 gold
- HTTPS: 330 alive / 81 gold
- SOCKS4: 222 alive / 128 gold
- SOCKS5: 214 alive / 140 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19778
- Ever gold: 797

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
