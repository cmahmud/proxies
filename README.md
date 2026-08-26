# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 408
- HTTP: 100 alive / 62 gold
- HTTPS: 77 alive / 19 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38473
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
