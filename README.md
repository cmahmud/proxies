# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 417
- HTTP: 101 alive / 72 gold
- HTTPS: 119 alive / 20 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41925
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
