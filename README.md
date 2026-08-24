# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 392
- HTTP: 118 alive / 54 gold
- HTTPS: 47 alive / 14 gold
- SOCKS4: 183 alive / 156 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33620
- Ever gold: 1244

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
