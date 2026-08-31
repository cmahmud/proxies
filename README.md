# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 417
- HTTP: 85 alive / 58 gold
- HTTPS: 68 alive / 26 gold
- SOCKS4: 185 alive / 164 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45499
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
