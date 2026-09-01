# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 406
- HTTP: 82 alive / 63 gold
- HTTPS: 99 alive / 23 gold
- SOCKS4: 165 alive / 158 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47212
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
