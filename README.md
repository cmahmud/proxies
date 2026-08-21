# SyndProxy private pool

## Current pool

- Alive now: 1024
- Gold now: 407
- HTTP: 345 alive / 101 gold
- HTTPS: 194 alive / 21 gold
- SOCKS4: 221 alive / 133 gold
- SOCKS5: 264 alive / 152 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27934
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
