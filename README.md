# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 434
- HTTP: 99 alive / 76 gold
- HTTPS: 70 alive / 29 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44426
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
