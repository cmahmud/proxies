# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 428
- HTTP: 130 alive / 84 gold
- HTTPS: 76 alive / 32 gold
- SOCKS4: 156 alive / 151 gold
- SOCKS5: 177 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44085
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
