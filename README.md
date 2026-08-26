# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 396
- HTTP: 100 alive / 63 gold
- HTTPS: 64 alive / 16 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 189 alive / 159 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38705
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
