# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 414
- HTTP: 107 alive / 67 gold
- HTTPS: 67 alive / 20 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35358
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
