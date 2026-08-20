# SyndProxy private pool

## Current pool

- Alive now: 966
- Gold now: 381
- HTTP: 288 alive / 94 gold
- HTTPS: 219 alive / 25 gold
- SOCKS4: 220 alive / 129 gold
- SOCKS5: 239 alive / 133 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25068
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
