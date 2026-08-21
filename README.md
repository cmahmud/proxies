# SyndProxy private pool

## Current pool

- Alive now: 923
- Gold now: 366
- HTTP: 280 alive / 82 gold
- HTTPS: 230 alive / 26 gold
- SOCKS4: 210 alive / 124 gold
- SOCKS5: 203 alive / 134 gold

## Historical pool

- Discovered: 158214
- Ever alive: 29803
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
