# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 449
- HTTP: 101 alive / 76 gold
- HTTPS: 105 alive / 31 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 191 alive / 180 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47390
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
