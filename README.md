# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 427
- HTTP: 102 alive / 75 gold
- HTTPS: 55 alive / 24 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 193 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44459
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
