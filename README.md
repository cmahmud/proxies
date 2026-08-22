# SyndProxy private pool

## Current pool

- Alive now: 925
- Gold now: 412
- HTTP: 286 alive / 83 gold
- HTTPS: 181 alive / 30 gold
- SOCKS4: 207 alive / 137 gold
- SOCKS5: 251 alive / 162 gold

## Historical pool

- Discovered: 162746
- Ever alive: 31505
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
