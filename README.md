# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 393
- HTTP: 110 alive / 65 gold
- HTTPS: 77 alive / 17 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 161 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37470
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
