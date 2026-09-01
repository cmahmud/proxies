# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 421
- HTTP: 88 alive / 67 gold
- HTTPS: 97 alive / 29 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 177 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47264
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
