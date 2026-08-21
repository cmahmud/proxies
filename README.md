# SyndProxy private pool

## Current pool

- Alive now: 960
- Gold now: 397
- HTTP: 319 alive / 95 gold
- HTTPS: 196 alive / 26 gold
- SOCKS4: 196 alive / 135 gold
- SOCKS5: 249 alive / 141 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27894
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
