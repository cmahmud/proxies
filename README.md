# SyndProxy validated proxy pool

## Current pool

- Alive now: 465
- Gold now: 408
- HTTP: 78 alive / 53 gold
- HTTPS: 38 alive / 21 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 177 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47108
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
