# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 125
- HTTP: 192 alive / 40 gold
- HTTPS: 80 alive / 4 gold
- SOCKS4: 157 alive / 0 gold
- SOCKS5: 202 alive / 81 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32679
- Ever gold: 1194

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
