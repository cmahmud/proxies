# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 386
- HTTP: 105 alive / 60 gold
- HTTPS: 37 alive / 11 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 190 alive / 156 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33315
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
