# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 386
- HTTP: 102 alive / 59 gold
- HTTPS: 48 alive / 18 gold
- SOCKS4: 157 alive / 152 gold
- SOCKS5: 176 alive / 157 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38934
- Ever gold: 1294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
