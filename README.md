# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 383
- HTTP: 107 alive / 59 gold
- HTTPS: 34 alive / 10 gold
- SOCKS4: 177 alive / 155 gold
- SOCKS5: 179 alive / 159 gold

## Historical pool

- Discovered: 174823
- Ever alive: 33103
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
