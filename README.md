# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 465
- HTTP: 133 alive / 100 gold
- HTTPS: 60 alive / 34 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49331
- Ever gold: 1578

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
