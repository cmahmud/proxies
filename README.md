# SyndProxy private pool

## Current pool

- Alive now: 1152
- Gold now: 602
- HTTP: 453 alive / 192 gold
- HTTPS: 259 alive / 111 gold
- SOCKS4: 218 alive / 144 gold
- SOCKS5: 222 alive / 155 gold

## Historical pool

- Discovered: 124852
- Ever alive: 19417
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
