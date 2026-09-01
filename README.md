# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 407
- HTTP: 77 alive / 58 gold
- HTTPS: 48 alive / 19 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47080
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
