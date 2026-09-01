# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 427
- HTTP: 114 alive / 74 gold
- HTTPS: 76 alive / 28 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 178 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47051
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
