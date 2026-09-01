# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 455
- HTTP: 124 alive / 83 gold
- HTTPS: 130 alive / 34 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 195 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46749
- Ever gold: 1449

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
