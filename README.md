# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 257
- HTTP: 128 alive / 36 gold
- HTTPS: 56 alive / 4 gold
- SOCKS4: 166 alive / 89 gold
- SOCKS5: 179 alive / 128 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32785
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
