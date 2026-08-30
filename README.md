# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 435
- HTTP: 127 alive / 84 gold
- HTTPS: 69 alive / 26 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44301
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
