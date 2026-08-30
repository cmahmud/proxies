# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 431
- HTTP: 112 alive / 80 gold
- HTTPS: 56 alive / 24 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44539
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
