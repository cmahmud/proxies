# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 429
- HTTP: 116 alive / 79 gold
- HTTPS: 56 alive / 24 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 190 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44541
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
