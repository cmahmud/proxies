# SyndProxy private pool

## Current pool

- Alive now: 988
- Gold now: 342
- HTTP: 339 alive / 64 gold
- HTTPS: 206 alive / 12 gold
- SOCKS4: 225 alive / 141 gold
- SOCKS5: 218 alive / 125 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20243
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
