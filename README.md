# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 376
- HTTP: 125 alive / 92 gold
- HTTPS: 40 alive / 33 gold
- SOCKS4: 89 alive / 75 gold
- SOCKS5: 223 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48646
- Ever gold: 1562

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
