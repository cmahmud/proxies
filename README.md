# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 439
- HTTP: 120 alive / 90 gold
- HTTPS: 65 alive / 31 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 175 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44095
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
