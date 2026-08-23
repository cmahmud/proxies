# SyndProxy validated proxy pool

## Current pool

- Alive now: 384
- Gold now: 207
- HTTP: 118 alive / 49 gold
- HTTPS: 75 alive / 8 gold
- SOCKS4: 77 alive / 67 gold
- SOCKS5: 114 alive / 83 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32697
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
