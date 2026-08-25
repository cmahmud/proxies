# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 426
- HTTP: 118 alive / 77 gold
- HTTPS: 98 alive / 23 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34888
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
