# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 423
- HTTP: 131 alive / 73 gold
- HTTPS: 86 alive / 23 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 196 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35204
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
