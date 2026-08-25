# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 417
- HTTP: 90 alive / 60 gold
- HTTPS: 74 alive / 22 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 192 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36202
- Ever gold: 1269

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
