# SyndProxy private pool

## Current pool

- Alive now: 1041
- Gold now: 385
- HTTP: 337 alive / 99 gold
- HTTPS: 226 alive / 22 gold
- SOCKS4: 234 alive / 130 gold
- SOCKS5: 244 alive / 134 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25075
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
