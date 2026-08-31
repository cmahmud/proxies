# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 426
- HTTP: 87 alive / 66 gold
- HTTPS: 60 alive / 29 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 196 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45477
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
