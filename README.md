# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 389
- HTTP: 125 alive / 52 gold
- HTTPS: 41 alive / 13 gold
- SOCKS4: 182 alive / 156 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33622
- Ever gold: 1244

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
