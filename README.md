# SyndProxy private pool

## Current pool

- Alive now: 852
- Gold now: 360
- HTTP: 248 alive / 80 gold
- HTTPS: 212 alive / 23 gold
- SOCKS4: 198 alive / 125 gold
- SOCKS5: 194 alive / 132 gold

## Historical pool

- Discovered: 158214
- Ever alive: 29802
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
