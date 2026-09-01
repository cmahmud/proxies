# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 411
- HTTP: 85 alive / 62 gold
- HTTPS: 101 alive / 25 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 179 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47225
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
