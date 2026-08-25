# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 418
- HTTP: 123 alive / 72 gold
- HTTPS: 105 alive / 19 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 190 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35284
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
