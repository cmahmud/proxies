# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 420
- HTTP: 103 alive / 78 gold
- HTTPS: 47 alive / 17 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44486
- Ever gold: 1402

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
