# SyndProxy private pool

## Current pool

- Alive now: 748
- Gold now: 396
- HTTP: 225 alive / 93 gold
- HTTPS: 116 alive / 21 gold
- SOCKS4: 177 alive / 123 gold
- SOCKS5: 230 alive / 159 gold

## Historical pool

- Discovered: 156424
- Ever alive: 29482
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
