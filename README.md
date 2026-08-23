# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 362
- HTTP: 107 alive / 37 gold
- HTTPS: 67 alive / 9 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 191 alive / 156 gold

## Historical pool

- Discovered: 171582
- Ever alive: 32922
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
