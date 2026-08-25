# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 398
- HTTP: 101 alive / 63 gold
- HTTPS: 78 alive / 18 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 175 alive / 158 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37551
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
