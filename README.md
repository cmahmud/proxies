# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 411
- HTTP: 83 alive / 62 gold
- HTTPS: 96 alive / 25 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 178 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47225
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
