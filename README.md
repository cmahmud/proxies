# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 467
- HTTP: 139 alive / 95 gold
- HTTPS: 120 alive / 34 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 200 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46315
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
