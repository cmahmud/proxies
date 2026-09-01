# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 438
- HTTP: 96 alive / 72 gold
- HTTPS: 115 alive / 30 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 191 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47341
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
