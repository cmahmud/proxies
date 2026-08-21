# SyndProxy private pool

## Current pool

- Alive now: 952
- Gold now: 409
- HTTP: 264 alive / 90 gold
- HTTPS: 197 alive / 25 gold
- SOCKS4: 243 alive / 147 gold
- SOCKS5: 248 alive / 147 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29100
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
