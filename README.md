# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 361
- HTTP: 106 alive / 37 gold
- HTTPS: 76 alive / 9 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 191 alive / 156 gold

## Historical pool

- Discovered: 171582
- Ever alive: 32921
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
