# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 444
- HTTP: 115 alive / 82 gold
- HTTPS: 117 alive / 30 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 197 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45637
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
