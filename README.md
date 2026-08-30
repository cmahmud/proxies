# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 446
- HTTP: 125 alive / 87 gold
- HTTPS: 74 alive / 36 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 198 alive / 164 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44277
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
