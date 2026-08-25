# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 427
- HTTP: 119 alive / 75 gold
- HTTPS: 89 alive / 23 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35163
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
