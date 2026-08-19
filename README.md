# SyndProxy private pool

## Current pool

- Alive now: 1080
- Gold now: 403
- HTTP: 317 alive / 90 gold
- HTTPS: 216 alive / 15 gold
- SOCKS4: 257 alive / 147 gold
- SOCKS5: 290 alive / 151 gold

## Historical pool

- Discovered: 131828
- Ever alive: 21082
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
