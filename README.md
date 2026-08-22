# SyndProxy private pool

## Current pool

- Alive now: 935
- Gold now: 399
- HTTP: 269 alive / 90 gold
- HTTPS: 205 alive / 30 gold
- SOCKS4: 225 alive / 147 gold
- SOCKS5: 236 alive / 132 gold

## Historical pool

- Discovered: 161987
- Ever alive: 31297
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
