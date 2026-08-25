# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 419
- HTTP: 123 alive / 70 gold
- HTTPS: 97 alive / 23 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35114
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
