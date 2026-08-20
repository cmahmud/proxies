# SyndProxy private pool

## Current pool

- Alive now: 665
- Gold now: 350
- HTTP: 192 alive / 67 gold
- HTTPS: 101 alive / 14 gold
- SOCKS4: 186 alive / 134 gold
- SOCKS5: 186 alive / 135 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25789
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
