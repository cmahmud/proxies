# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 433
- HTTP: 127 alive / 86 gold
- HTTPS: 77 alive / 35 gold
- SOCKS4: 154 alive / 151 gold
- SOCKS5: 177 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44085
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
