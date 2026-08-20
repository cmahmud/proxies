# SyndProxy private pool

## Current pool

- Alive now: 1078
- Gold now: 571
- HTTP: 338 alive / 188 gold
- HTTPS: 270 alive / 97 gold
- SOCKS4: 231 alive / 136 gold
- SOCKS5: 239 alive / 150 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23251
- Ever gold: 916

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
