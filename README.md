# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 422
- HTTP: 118 alive / 71 gold
- HTTPS: 72 alive / 27 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 199 alive / 164 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44347
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
