# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 440
- HTTP: 98 alive / 71 gold
- HTTPS: 95 alive / 30 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 188 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47445
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
