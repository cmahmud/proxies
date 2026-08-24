# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 382
- HTTP: 105 alive / 46 gold
- HTTPS: 56 alive / 13 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 180671
- Ever alive: 33574
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
