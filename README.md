# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 392
- HTTP: 96 alive / 58 gold
- HTTPS: 67 alive / 15 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 176 alive / 160 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33501
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
