# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 408
- HTTP: 90 alive / 59 gold
- HTTPS: 105 alive / 20 gold
- SOCKS4: 181 alive / 164 gold
- SOCKS5: 194 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41506
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
