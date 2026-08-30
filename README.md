# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 438
- HTTP: 121 alive / 89 gold
- HTTPS: 66 alive / 36 gold
- SOCKS4: 154 alive / 152 gold
- SOCKS5: 177 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44088
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
