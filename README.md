# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 386
- HTTP: 119 alive / 68 gold
- HTTPS: 48 alive / 14 gold
- SOCKS4: 166 alive / 153 gold
- SOCKS5: 175 alive / 151 gold

## Historical pool

- Discovered: 176956
- Ever alive: 33250
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
