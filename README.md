# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 417
- HTTP: 103 alive / 70 gold
- HTTPS: 84 alive / 23 gold
- SOCKS4: 164 alive / 157 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34985
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
