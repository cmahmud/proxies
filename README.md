# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 418
- HTTP: 105 alive / 71 gold
- HTTPS: 105 alive / 19 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35262
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
