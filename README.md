# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 402
- HTTP: 100 alive / 58 gold
- HTTPS: 69 alive / 18 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38997
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
