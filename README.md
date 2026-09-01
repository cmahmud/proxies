# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 466
- HTTP: 122 alive / 88 gold
- HTTPS: 103 alive / 42 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 186 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46971
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
