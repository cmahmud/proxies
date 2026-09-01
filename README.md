# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 405
- HTTP: 73 alive / 52 gold
- HTTPS: 47 alive / 19 gold
- SOCKS4: 174 alive / 164 gold
- SOCKS5: 180 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47105
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
