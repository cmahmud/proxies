# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 409
- HTTP: 85 alive / 61 gold
- HTTPS: 100 alive / 25 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 175 alive / 165 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47213
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
