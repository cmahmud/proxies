# SyndProxy private pool

## Current pool

- Alive now: 935
- Gold now: 405
- HTTP: 278 alive / 87 gold
- HTTPS: 191 alive / 21 gold
- SOCKS4: 210 alive / 141 gold
- SOCKS5: 256 alive / 156 gold

## Historical pool

- Discovered: 163863
- Ever alive: 31969
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
