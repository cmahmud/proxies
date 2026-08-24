# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 433
- HTTP: 105 alive / 77 gold
- HTTPS: 65 alive / 24 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 205 alive / 170 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34087
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
