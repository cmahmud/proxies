# SyndProxy private pool

## Current pool

- Alive now: 1069
- Gold now: 421
- HTTP: 357 alive / 104 gold
- HTTPS: 251 alive / 35 gold
- SOCKS4: 221 alive / 140 gold
- SOCKS5: 240 alive / 142 gold

## Historical pool

- Discovered: 160257
- Ever alive: 30691
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
