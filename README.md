# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 423
- HTTP: 85 alive / 67 gold
- HTTPS: 91 alive / 26 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 179 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47132
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
