# SyndProxy validated proxy pool

## Current pool

- Alive now: 388
- Gold now: 208
- HTTP: 127 alive / 50 gold
- HTTPS: 51 alive / 8 gold
- SOCKS4: 91 alive / 67 gold
- SOCKS5: 119 alive / 83 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32696
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
