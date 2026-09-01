# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 427
- HTTP: 110 alive / 68 gold
- HTTPS: 68 alive / 31 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 174 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47056
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
