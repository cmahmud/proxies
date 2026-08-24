# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 432
- HTTP: 130 alive / 78 gold
- HTTPS: 85 alive / 24 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34672
- Ever gold: 1257

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
