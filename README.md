# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 434
- HTTP: 138 alive / 80 gold
- HTTPS: 102 alive / 24 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 195 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34558
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
