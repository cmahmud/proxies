# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 418
- HTTP: 117 alive / 74 gold
- HTTPS: 72 alive / 18 gold
- SOCKS4: 175 alive / 157 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34879
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
