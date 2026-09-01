# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 438
- HTTP: 105 alive / 75 gold
- HTTPS: 88 alive / 33 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 178 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47015
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
