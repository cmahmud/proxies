# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 438
- HTTP: 115 alive / 75 gold
- HTTPS: 96 alive / 33 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 178 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47015
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
