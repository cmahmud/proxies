# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 454
- HTTP: 102 alive / 78 gold
- HTTPS: 108 alive / 33 gold
- SOCKS4: 174 alive / 165 gold
- SOCKS5: 186 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47428
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
