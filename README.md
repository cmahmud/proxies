# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 444
- HTTP: 98 alive / 77 gold
- HTTPS: 103 alive / 30 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 191 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47356
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
