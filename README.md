# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 426
- HTTP: 103 alive / 74 gold
- HTTPS: 60 alive / 24 gold
- SOCKS4: 165 alive / 161 gold
- SOCKS5: 200 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44463
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
