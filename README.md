# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 431
- HTTP: 104 alive / 77 gold
- HTTPS: 54 alive / 27 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 191 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44458
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
