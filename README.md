# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 403
- HTTP: 142 alive / 71 gold
- HTTPS: 72 alive / 13 gold
- SOCKS4: 172 alive / 156 gold
- SOCKS5: 199 alive / 163 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33305
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
