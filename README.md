# SyndProxy validated proxy pool

## Current pool

- Alive now: 665
- Gold now: 404
- HTTP: 184 alive / 72 gold
- HTTPS: 85 alive / 15 gold
- SOCKS4: 190 alive / 156 gold
- SOCKS5: 206 alive / 161 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33302
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
