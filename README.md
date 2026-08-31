# SyndProxy validated proxy pool

## Current pool

- Alive now: 690
- Gold now: 468
- HTTP: 150 alive / 98 gold
- HTTPS: 131 alive / 33 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 229 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46232
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
