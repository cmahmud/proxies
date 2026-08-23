# SyndProxy validated proxy pool

## Current pool

- Alive now: 453
- Gold now: 377
- HTTP: 85 alive / 61 gold
- HTTPS: 29 alive / 8 gold
- SOCKS4: 163 alive / 154 gold
- SOCKS5: 176 alive / 154 gold

## Historical pool

- Discovered: 174811
- Ever alive: 33094
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
