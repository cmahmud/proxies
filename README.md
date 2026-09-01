# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 412
- HTTP: 76 alive / 61 gold
- HTTPS: 49 alive / 21 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 174 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47078
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
