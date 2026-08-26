# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 408
- HTTP: 107 alive / 69 gold
- HTTPS: 58 alive / 17 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 184 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38948
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
