# SyndProxy validated proxy pool

## Current pool

- Alive now: 694
- Gold now: 466
- HTTP: 142 alive / 94 gold
- HTTPS: 139 alive / 34 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 233 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46183
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
