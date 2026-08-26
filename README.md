# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 371
- HTTP: 93 alive / 58 gold
- HTTPS: 55 alive / 18 gold
- SOCKS4: 152 alive / 142 gold
- SOCKS5: 169 alive / 153 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38858
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
