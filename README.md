# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 417
- HTTP: 85 alive / 61 gold
- HTTPS: 41 alive / 22 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 183 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47094
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
