# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 392
- HTTP: 101 alive / 65 gold
- HTTPS: 73 alive / 20 gold
- SOCKS4: 169 alive / 155 gold
- SOCKS5: 163 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37484
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
