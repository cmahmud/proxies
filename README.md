# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 411
- HTTP: 107 alive / 59 gold
- HTTPS: 68 alive / 21 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45518
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
