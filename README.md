# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 383
- HTTP: 123 alive / 67 gold
- HTTPS: 54 alive / 14 gold
- SOCKS4: 171 alive / 151 gold
- SOCKS5: 180 alive / 151 gold

## Historical pool

- Discovered: 176956
- Ever alive: 33250
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
