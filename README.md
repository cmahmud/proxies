# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 376
- HTTP: 127 alive / 93 gold
- HTTPS: 40 alive / 33 gold
- SOCKS4: 89 alive / 75 gold
- SOCKS5: 224 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48645
- Ever gold: 1562

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
