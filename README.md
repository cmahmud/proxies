# SyndProxy private pool

## Current pool

- Alive now: 973
- Gold now: 403
- HTTP: 266 alive / 84 gold
- HTTPS: 215 alive / 23 gold
- SOCKS4: 243 alive / 147 gold
- SOCKS5: 249 alive / 149 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29108
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
