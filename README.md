# SyndProxy private pool

## Current pool

- Alive now: 1276
- Gold now: 397
- HTTP: 470 alive / 101 gold
- HTTPS: 318 alive / 26 gold
- SOCKS4: 226 alive / 125 gold
- SOCKS5: 262 alive / 145 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28097
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
