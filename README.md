# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 425
- HTTP: 106 alive / 73 gold
- HTTPS: 63 alive / 27 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44364
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
