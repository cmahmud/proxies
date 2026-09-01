# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 428
- HTTP: 80 alive / 70 gold
- HTTPS: 72 alive / 27 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 178 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47149
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
