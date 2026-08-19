# SyndProxy private pool

## Current pool

- Alive now: 1077
- Gold now: 479
- HTTP: 378 alive / 122 gold
- HTTPS: 239 alive / 73 gold
- SOCKS4: 214 alive / 143 gold
- SOCKS5: 246 alive / 141 gold

## Historical pool

- Discovered: 113910
- Ever alive: 16897
- Ever gold: 626

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
