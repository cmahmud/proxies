# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 438
- HTTP: 128 alive / 82 gold
- HTTPS: 76 alive / 29 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44300
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
