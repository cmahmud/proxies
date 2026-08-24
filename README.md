# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 437
- HTTP: 123 alive / 80 gold
- HTTPS: 72 alive / 25 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 189 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34697
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
