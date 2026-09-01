# SyndProxy validated proxy pool

## Current pool

- Alive now: 611
- Gold now: 453
- HTTP: 128 alive / 85 gold
- HTTPS: 124 alive / 30 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 189 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46786
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
