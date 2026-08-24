# SyndProxy validated proxy pool

## Current pool

- Alive now: 593
- Gold now: 403
- HTTP: 143 alive / 68 gold
- HTTPS: 53 alive / 14 gold
- SOCKS4: 182 alive / 157 gold
- SOCKS5: 215 alive / 164 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33293
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
