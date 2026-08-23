# SyndProxy validated proxy pool

## Current pool

- Alive now: 391
- Gold now: 210
- HTTP: 131 alive / 52 gold
- HTTPS: 50 alive / 8 gold
- SOCKS4: 91 alive / 67 gold
- SOCKS5: 119 alive / 83 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32696
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
