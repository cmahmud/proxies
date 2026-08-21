# SyndProxy private pool

## Current pool

- Alive now: 821
- Gold now: 428
- HTTP: 233 alive / 93 gold
- HTTPS: 106 alive / 20 gold
- SOCKS4: 238 alive / 157 gold
- SOCKS5: 244 alive / 158 gold

## Historical pool

- Discovered: 157425
- Ever alive: 29752
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
