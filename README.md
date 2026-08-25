# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 390
- HTTP: 103 alive / 64 gold
- HTTPS: 74 alive / 19 gold
- SOCKS4: 168 alive / 155 gold
- SOCKS5: 162 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37486
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
