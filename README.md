# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 417
- HTTP: 102 alive / 74 gold
- HTTPS: 109 alive / 19 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 178 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41998
- Ever gold: 1347

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
