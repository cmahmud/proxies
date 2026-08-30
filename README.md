# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 438
- HTTP: 121 alive / 88 gold
- HTTPS: 62 alive / 32 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 174 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44095
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
