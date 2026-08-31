# SyndProxy validated proxy pool

## Current pool

- Alive now: 662
- Gold now: 461
- HTTP: 134 alive / 95 gold
- HTTPS: 135 alive / 30 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 220 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46122
- Ever gold: 1440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
