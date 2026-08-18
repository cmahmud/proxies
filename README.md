# SyndProxy private pool

## Current pool

- Alive now: 952
- Gold now: 253
- HTTP: 393 alive / 27 gold
- HTTPS: 144 alive / 2 gold
- SOCKS4: 200 alive / 118 gold
- SOCKS5: 215 alive / 106 gold

## Historical pool

- Discovered: 99104
- Ever alive: 11737
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
