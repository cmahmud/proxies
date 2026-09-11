# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 374
- HTTP: 120 alive / 90 gold
- HTTPS: 40 alive / 33 gold
- SOCKS4: 87 alive / 76 gold
- SOCKS5: 213 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48646
- Ever gold: 1563

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
