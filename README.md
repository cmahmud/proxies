# SyndProxy private pool

## Current pool

- Alive now: 1012
- Gold now: 388
- HTTP: 367 alive / 81 gold
- HTTPS: 169 alive / 20 gold
- SOCKS4: 216 alive / 128 gold
- SOCKS5: 260 alive / 159 gold

## Historical pool

- Discovered: 157412
- Ever alive: 29705
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
