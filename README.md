# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 348
- HTTP: 112 alive / 41 gold
- HTTPS: 80 alive / 11 gold
- SOCKS4: 158 alive / 154 gold
- SOCKS5: 179 alive / 142 gold

## Historical pool

- Discovered: 171038
- Ever alive: 32813
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
