# SyndProxy validated proxy pool

## Current pool

- Alive now: 748
- Gold now: 460
- HTTP: 162 alive / 94 gold
- HTTPS: 148 alive / 30 gold
- SOCKS4: 185 alive / 162 gold
- SOCKS5: 253 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46274
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
