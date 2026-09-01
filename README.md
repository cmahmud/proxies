# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 455
- HTTP: 126 alive / 84 gold
- HTTPS: 127 alive / 31 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 191 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46752
- Ever gold: 1449

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
