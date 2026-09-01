# SyndProxy validated proxy pool

## Current pool

- Alive now: 467
- Gold now: 411
- HTTP: 76 alive / 61 gold
- HTTPS: 46 alive / 20 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 173 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47078
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
