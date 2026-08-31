# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 421
- HTTP: 86 alive / 58 gold
- HTTPS: 64 alive / 30 gold
- SOCKS4: 184 alive / 162 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45498
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
