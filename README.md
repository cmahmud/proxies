# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 421
- HTTP: 120 alive / 72 gold
- HTTPS: 91 alive / 22 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34934
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
