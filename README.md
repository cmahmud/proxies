# SyndProxy private pool

## Current pool

- Alive now: 1110
- Gold now: 411
- HTTP: 392 alive / 106 gold
- HTTPS: 278 alive / 31 gold
- SOCKS4: 198 alive / 124 gold
- SOCKS5: 242 alive / 150 gold

## Historical pool

- Discovered: 152761
- Ever alive: 28363
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
