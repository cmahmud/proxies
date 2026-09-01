# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 422
- HTTP: 90 alive / 67 gold
- HTTPS: 99 alive / 30 gold
- SOCKS4: 165 alive / 157 gold
- SOCKS5: 178 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47266
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
