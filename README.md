# SyndProxy validated proxy pool

## Current pool

- Alive now: 735
- Gold now: 36
- HTTP: 243 alive / 30 gold
- HTTPS: 96 alive / 2 gold
- SOCKS4: 111 alive / 0 gold
- SOCKS5: 285 alive / 4 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32670
- Ever gold: 1192

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
