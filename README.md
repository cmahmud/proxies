# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 439
- HTTP: 124 alive / 93 gold
- HTTPS: 72 alive / 33 gold
- SOCKS4: 165 alive / 153 gold
- SOCKS5: 170 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44094
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
