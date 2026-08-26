# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 375
- HTTP: 97 alive / 66 gold
- HTTPS: 70 alive / 15 gold
- SOCKS4: 155 alive / 143 gold
- SOCKS5: 185 alive / 151 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38806
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
