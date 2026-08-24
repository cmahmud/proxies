# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 384
- HTTP: 103 alive / 57 gold
- HTTPS: 43 alive / 8 gold
- SOCKS4: 165 alive / 158 gold
- SOCKS5: 189 alive / 161 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33319
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
