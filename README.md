# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 428
- HTTP: 107 alive / 72 gold
- HTTPS: 55 alive / 27 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44448
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
