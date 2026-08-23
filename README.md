# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 392
- HTTP: 123 alive / 64 gold
- HTTPS: 60 alive / 14 gold
- SOCKS4: 168 alive / 152 gold
- SOCKS5: 188 alive / 162 gold

## Historical pool

- Discovered: 175451
- Ever alive: 33163
- Ever gold: 1228

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
