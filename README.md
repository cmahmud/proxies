# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 359
- HTTP: 105 alive / 36 gold
- HTTPS: 74 alive / 8 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 192 alive / 156 gold

## Historical pool

- Discovered: 171582
- Ever alive: 32921
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
