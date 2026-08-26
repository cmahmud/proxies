# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 371
- HTTP: 98 alive / 56 gold
- HTTPS: 61 alive / 18 gold
- SOCKS4: 153 alive / 143 gold
- SOCKS5: 174 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38891
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
