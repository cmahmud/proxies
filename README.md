# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 430
- HTTP: 117 alive / 78 gold
- HTTPS: 99 alive / 23 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34892
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
