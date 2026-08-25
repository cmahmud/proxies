# SyndProxy validated proxy pool

## Current pool

- Alive now: 593
- Gold now: 428
- HTTP: 122 alive / 75 gold
- HTTPS: 101 alive / 24 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 192 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35173
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
