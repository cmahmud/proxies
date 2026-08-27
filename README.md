# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 417
- HTTP: 97 alive / 73 gold
- HTTPS: 114 alive / 20 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 180 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42000
- Ever gold: 1347

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
