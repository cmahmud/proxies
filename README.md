# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 384
- HTTP: 110 alive / 54 gold
- HTTPS: 52 alive / 12 gold
- SOCKS4: 171 alive / 156 gold
- SOCKS5: 183 alive / 162 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33470
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
