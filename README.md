# SyndProxy validated proxy pool

## Current pool

- Alive now: 667
- Gold now: 330
- HTTP: 136 alive / 76 gold
- HTTPS: 102 alive / 31 gold
- SOCKS4: 100 alive / 53 gold
- SOCKS5: 329 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48555
- Ever gold: 1545

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
