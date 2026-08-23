# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 225
- HTTP: 150 alive / 37 gold
- HTTPS: 78 alive / 6 gold
- SOCKS4: 166 alive / 90 gold
- SOCKS5: 183 alive / 92 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32785
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
