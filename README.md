# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 219
- HTTP: 148 alive / 37 gold
- HTTPS: 75 alive / 5 gold
- SOCKS4: 166 alive / 85 gold
- SOCKS5: 183 alive / 92 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32785
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
