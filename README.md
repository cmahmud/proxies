# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 467
- HTTP: 131 alive / 90 gold
- HTTPS: 106 alive / 37 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 198 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46351
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
