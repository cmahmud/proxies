# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 396
- HTTP: 149 alive / 66 gold
- HTTPS: 62 alive / 15 gold
- SOCKS4: 165 alive / 154 gold
- SOCKS5: 189 alive / 161 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33285
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
