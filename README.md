# SyndProxy validated proxy pool

## Current pool

- Alive now: 391
- Gold now: 208
- HTTP: 121 alive / 51 gold
- HTTPS: 77 alive / 7 gold
- SOCKS4: 78 alive / 67 gold
- SOCKS5: 115 alive / 83 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32697
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
