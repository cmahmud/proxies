# SyndProxy private pool

## Current pool

- Alive now: 1048
- Gold now: 394
- HTTP: 331 alive / 100 gold
- HTTPS: 207 alive / 27 gold
- SOCKS4: 245 alive / 131 gold
- SOCKS5: 265 alive / 136 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25093
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
