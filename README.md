# SyndProxy private pool

## Current pool

- Alive now: 972
- Gold now: 403
- HTTP: 266 alive / 85 gold
- HTTPS: 216 alive / 23 gold
- SOCKS4: 245 alive / 147 gold
- SOCKS5: 245 alive / 148 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29107
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
