# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 348
- HTTP: 113 alive / 39 gold
- HTTPS: 58 alive / 10 gold
- SOCKS4: 169 alive / 152 gold
- SOCKS5: 176 alive / 147 gold

## Historical pool

- Discovered: 171048
- Ever alive: 32852
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
