# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 407
- HTTP: 77 alive / 54 gold
- HTTPS: 46 alive / 20 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 182 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47115
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
