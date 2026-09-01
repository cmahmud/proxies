# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 417
- HTTP: 96 alive / 64 gold
- HTTPS: 46 alive / 22 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 176 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47085
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
