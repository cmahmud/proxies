# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 426
- HTTP: 131 alive / 73 gold
- HTTPS: 103 alive / 25 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35177
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
