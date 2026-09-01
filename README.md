# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 443
- HTTP: 110 alive / 79 gold
- HTTPS: 89 alive / 32 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47008
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
