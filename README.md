# SyndProxy validated proxy pool

## Current pool

- Alive now: 739
- Gold now: 462
- HTTP: 161 alive / 95 gold
- HTTPS: 145 alive / 31 gold
- SOCKS4: 185 alive / 162 gold
- SOCKS5: 248 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46275
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
