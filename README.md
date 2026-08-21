# SyndProxy private pool

## Current pool

- Alive now: 1072
- Gold now: 373
- HTTP: 359 alive / 105 gold
- HTTPS: 251 alive / 31 gold
- SOCKS4: 206 alive / 112 gold
- SOCKS5: 256 alive / 125 gold

## Historical pool

- Discovered: 152755
- Ever alive: 28302
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
