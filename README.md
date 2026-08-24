# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 386
- HTTP: 115 alive / 49 gold
- HTTPS: 68 alive / 15 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33611
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
