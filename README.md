# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 414
- HTTP: 106 alive / 67 gold
- HTTPS: 74 alive / 18 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 189 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35338
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
