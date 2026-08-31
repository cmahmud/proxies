# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 417
- HTTP: 94 alive / 63 gold
- HTTPS: 67 alive / 25 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 196 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45477
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
