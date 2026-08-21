# SyndProxy private pool

## Current pool

- Alive now: 904
- Gold now: 402
- HTTP: 283 alive / 91 gold
- HTTPS: 161 alive / 20 gold
- SOCKS4: 218 alive / 151 gold
- SOCKS5: 242 alive / 140 gold

## Historical pool

- Discovered: 155695
- Ever alive: 29232
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
