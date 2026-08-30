# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 447
- HTTP: 147 alive / 86 gold
- HTTPS: 79 alive / 34 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 208 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44224
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
