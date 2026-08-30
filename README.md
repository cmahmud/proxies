# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 437
- HTTP: 129 alive / 90 gold
- HTTPS: 79 alive / 34 gold
- SOCKS4: 161 alive / 152 gold
- SOCKS5: 174 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44077
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
