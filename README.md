# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 414
- HTTP: 101 alive / 63 gold
- HTTPS: 80 alive / 22 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35486
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
