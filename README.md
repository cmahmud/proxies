# SyndProxy private pool

## Current pool

- Alive now: 908
- Gold now: 404
- HTTP: 280 alive / 81 gold
- HTTPS: 177 alive / 29 gold
- SOCKS4: 203 alive / 131 gold
- SOCKS5: 248 alive / 163 gold

## Historical pool

- Discovered: 162746
- Ever alive: 31505
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
