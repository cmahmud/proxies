# SyndProxy private pool

## Current pool

- Alive now: 1096
- Gold now: 305
- HTTP: 401 alive / 31 gold
- HTTPS: 255 alive / 4 gold
- SOCKS4: 231 alive / 142 gold
- SOCKS5: 209 alive / 128 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13438
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
