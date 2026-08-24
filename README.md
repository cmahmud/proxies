# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 434
- HTTP: 125 alive / 80 gold
- HTTPS: 68 alive / 22 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34694
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
