# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 430
- HTTP: 116 alive / 76 gold
- HTTPS: 65 alive / 26 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44456
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
