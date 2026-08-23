# SyndProxy validated proxy pool

## Current pool

- Alive now: 386
- Gold now: 205
- HTTP: 118 alive / 50 gold
- HTTPS: 77 alive / 7 gold
- SOCKS4: 77 alive / 65 gold
- SOCKS5: 114 alive / 83 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32697
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
