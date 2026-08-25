# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 426
- HTTP: 106 alive / 75 gold
- HTTPS: 98 alive / 23 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35010
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
