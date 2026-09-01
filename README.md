# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 468
- HTTP: 141 alive / 95 gold
- HTTPS: 126 alive / 39 gold
- SOCKS4: 183 alive / 163 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46918
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
