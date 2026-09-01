# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 407
- HTTP: 86 alive / 59 gold
- HTTPS: 45 alive / 20 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 180 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47081
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
