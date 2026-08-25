# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 402
- HTTP: 102 alive / 69 gold
- HTTPS: 76 alive / 20 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 168 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37452
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
