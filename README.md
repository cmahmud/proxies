# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 417
- HTTP: 85 alive / 67 gold
- HTTPS: 66 alive / 25 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47165
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
