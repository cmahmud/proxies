# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 467
- HTTP: 125 alive / 87 gold
- HTTPS: 102 alive / 42 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 186 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46971
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
