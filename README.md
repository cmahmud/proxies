# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 392
- HTTP: 137 alive / 54 gold
- HTTPS: 42 alive / 13 gold
- SOCKS4: 180 alive / 156 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33628
- Ever gold: 1244

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
