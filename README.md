# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 399
- HTTP: 119 alive / 67 gold
- HTTPS: 50 alive / 12 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 193 alive / 161 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33315
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
