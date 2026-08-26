# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 376
- HTTP: 109 alive / 65 gold
- HTTPS: 71 alive / 20 gold
- SOCKS4: 146 alive / 140 gold
- SOCKS5: 171 alive / 151 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38764
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
