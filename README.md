# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 435
- HTTP: 128 alive / 82 gold
- HTTPS: 93 alive / 23 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34776
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
