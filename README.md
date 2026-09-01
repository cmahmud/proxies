# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 418
- HTTP: 89 alive / 66 gold
- HTTPS: 64 alive / 24 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47072
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
