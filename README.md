# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 403
- HTTP: 114 alive / 63 gold
- HTTPS: 43 alive / 15 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33662
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
