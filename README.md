# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 416
- HTTP: 82 alive / 61 gold
- HTTPS: 43 alive / 22 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47088
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
