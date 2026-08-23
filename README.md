# SyndProxy validated proxy pool

## Current pool

- Alive now: 587
- Gold now: 346
- HTTP: 129 alive / 38 gold
- HTTPS: 94 alive / 5 gold
- SOCKS4: 167 alive / 152 gold
- SOCKS5: 197 alive / 151 gold

## Historical pool

- Discovered: 171582
- Ever alive: 32915
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
