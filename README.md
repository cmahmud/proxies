# SyndProxy validated proxy pool

## Current pool

- Alive now: 383
- Gold now: 321
- HTTP: 83 alive / 64 gold
- HTTPS: 35 alive / 21 gold
- SOCKS4: 116 alive / 108 gold
- SOCKS5: 149 alive / 128 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49488
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
