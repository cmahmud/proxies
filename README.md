# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 417
- HTTP: 114 alive / 68 gold
- HTTPS: 67 alive / 20 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35411
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
