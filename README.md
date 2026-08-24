# SyndProxy validated proxy pool

## Current pool

- Alive now: 600
- Gold now: 437
- HTTP: 139 alive / 82 gold
- HTTPS: 95 alive / 25 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34580
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
