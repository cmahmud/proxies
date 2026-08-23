# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 361
- HTTP: 109 alive / 37 gold
- HTTPS: 56 alive / 9 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 190 alive / 155 gold

## Historical pool

- Discovered: 171582
- Ever alive: 32925
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
