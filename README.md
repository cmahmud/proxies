# SyndProxy private pool

## Current pool

- Alive now: 986
- Gold now: 215
- HTTP: 401 alive / 31 gold
- HTTPS: 154 alive / 7 gold
- SOCKS4: 244 alive / 103 gold
- SOCKS5: 187 alive / 74 gold

## Historical pool

- Discovered: 86675
- Ever alive: 6452
- Ever gold: 296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
