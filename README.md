# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 361
- HTTP: 104 alive / 37 gold
- HTTPS: 81 alive / 8 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 197 alive / 156 gold

## Historical pool

- Discovered: 171582
- Ever alive: 32920
- Ever gold: 1215

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
