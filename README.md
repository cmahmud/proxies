# SyndProxy private pool

## Current pool

- Alive now: 976
- Gold now: 398
- HTTP: 298 alive / 94 gold
- HTTPS: 218 alive / 33 gold
- SOCKS4: 213 alive / 144 gold
- SOCKS5: 247 alive / 127 gold

## Historical pool

- Discovered: 160994
- Ever alive: 30915
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
