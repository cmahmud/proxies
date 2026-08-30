# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 413
- HTTP: 111 alive / 72 gold
- HTTPS: 44 alive / 18 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 189 alive / 163 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44483
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
