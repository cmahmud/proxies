# SyndProxy private pool

## Current pool

- Alive now: 952
- Gold now: 417
- HTTP: 293 alive / 83 gold
- HTTPS: 197 alive / 25 gold
- SOCKS4: 216 alive / 149 gold
- SOCKS5: 246 alive / 160 gold

## Historical pool

- Discovered: 154339
- Ever alive: 28905
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
