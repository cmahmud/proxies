# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 358
- HTTP: 86 alive / 33 gold
- HTTPS: 48 alive / 10 gold
- SOCKS4: 166 alive / 154 gold
- SOCKS5: 179 alive / 161 gold

## Historical pool

- Discovered: 171600
- Ever alive: 32943
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
