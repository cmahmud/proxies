# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 419
- HTTP: 84 alive / 67 gold
- HTTPS: 72 alive / 26 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47166
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
