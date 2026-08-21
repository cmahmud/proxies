# SyndProxy private pool

## Current pool

- Alive now: 1075
- Gold now: 453
- HTTP: 362 alive / 101 gold
- HTTPS: 237 alive / 33 gold
- SOCKS4: 206 alive / 148 gold
- SOCKS5: 270 alive / 171 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28706
- Ever gold: 1112

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
