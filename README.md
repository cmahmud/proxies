# SyndProxy validated proxy pool

## Current pool

- Alive now: 663
- Gold now: 358
- HTTP: 122 alive / 80 gold
- HTTPS: 79 alive / 29 gold
- SOCKS4: 220 alive / 69 gold
- SOCKS5: 242 alive / 180 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48578
- Ever gold: 1548

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
