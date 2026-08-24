# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 385
- HTTP: 96 alive / 58 gold
- HTTPS: 54 alive / 12 gold
- SOCKS4: 159 alive / 156 gold
- SOCKS5: 178 alive / 159 gold

## Historical pool

- Discovered: 175898
- Ever alive: 33196
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
