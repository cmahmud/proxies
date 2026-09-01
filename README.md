# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 460
- HTTP: 139 alive / 89 gold
- HTTPS: 141 alive / 35 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 188 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46691
- Ever gold: 1446

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
