# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 471
- HTTP: 150 alive / 94 gold
- HTTPS: 127 alive / 41 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 195 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46938
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
