# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 257
- HTTP: 446 alive / 29 gold
- HTTPS: 144 alive / 2 gold
- SOCKS4: 199 alive / 120 gold
- SOCKS5: 222 alive / 106 gold

## Historical pool

- Discovered: 99104
- Ever alive: 11744
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
