# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 407
- HTTP: 113 alive / 65 gold
- HTTPS: 46 alive / 15 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33661
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
