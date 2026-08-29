# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 375
- HTTP: 87 alive / 59 gold
- HTTPS: 75 alive / 11 gold
- SOCKS4: 161 alive / 154 gold
- SOCKS5: 167 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43351
- Ever gold: 1370

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
