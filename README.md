# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 431
- HTTP: 114 alive / 80 gold
- HTTPS: 58 alive / 24 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44540
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
