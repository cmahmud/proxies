# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 434
- HTTP: 120 alive / 78 gold
- HTTPS: 93 alive / 24 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 201 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45458
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
