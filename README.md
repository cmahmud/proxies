# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 428
- HTTP: 121 alive / 75 gold
- HTTPS: 97 alive / 24 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 194 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35170
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
