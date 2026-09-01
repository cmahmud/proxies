# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 450
- HTTP: 120 alive / 81 gold
- HTTPS: 89 alive / 35 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46999
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
