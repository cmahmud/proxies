# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 392
- HTTP: 92 alive / 68 gold
- HTTPS: 39 alive / 14 gold
- SOCKS4: 175 alive / 153 gold
- SOCKS5: 177 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48116
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
