# SyndProxy private pool

## Current pool

- Alive now: 748
- Gold now: 391
- HTTP: 223 alive / 88 gold
- HTTPS: 105 alive / 24 gold
- SOCKS4: 179 alive / 122 gold
- SOCKS5: 241 alive / 157 gold

## Historical pool

- Discovered: 156424
- Ever alive: 29478
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
