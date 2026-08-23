# SyndProxy validated proxy pool

## Current pool

- Alive now: 467
- Gold now: 378
- HTTP: 89 alive / 61 gold
- HTTPS: 34 alive / 10 gold
- SOCKS4: 165 alive / 152 gold
- SOCKS5: 179 alive / 155 gold

## Historical pool

- Discovered: 174811
- Ever alive: 33097
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
