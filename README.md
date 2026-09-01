# SyndProxy validated proxy pool

## Current pool

- Alive now: 607
- Gold now: 456
- HTTP: 118 alive / 87 gold
- HTTPS: 121 alive / 31 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 196 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46773
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
