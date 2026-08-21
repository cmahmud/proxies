# SyndProxy private pool

## Current pool

- Alive now: 1201
- Gold now: 417
- HTTP: 444 alive / 102 gold
- HTTPS: 264 alive / 27 gold
- SOCKS4: 240 alive / 138 gold
- SOCKS5: 253 alive / 150 gold

## Historical pool

- Discovered: 159282
- Ever alive: 30433
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
