# SyndProxy validated proxy pool

## Current pool

- Alive now: 383
- Gold now: 303
- HTTP: 102 alive / 74 gold
- HTTPS: 34 alive / 18 gold
- SOCKS4: 77 alive / 68 gold
- SOCKS5: 170 alive / 143 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47843
- Ever gold: 1498

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
