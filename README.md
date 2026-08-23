# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 334
- HTTP: 99 alive / 37 gold
- HTTPS: 80 alive / 5 gold
- SOCKS4: 163 alive / 150 gold
- SOCKS5: 187 alive / 142 gold

## Historical pool

- Discovered: 171582
- Ever alive: 32904
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
