# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 412
- HTTP: 81 alive / 63 gold
- HTTPS: 84 alive / 23 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47189
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
