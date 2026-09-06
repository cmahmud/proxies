# SyndProxy validated proxy pool

## Current pool

- Alive now: 431
- Gold now: 355
- HTTP: 83 alive / 67 gold
- HTTPS: 38 alive / 16 gold
- SOCKS4: 153 alive / 142 gold
- SOCKS5: 157 alive / 130 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48380
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
