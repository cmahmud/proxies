# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 382
- HTTP: 119 alive / 69 gold
- HTTPS: 151 alive / 20 gold
- SOCKS4: 164 alive / 145 gold
- SOCKS5: 182 alive / 148 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39641
- Ever gold: 1300

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
