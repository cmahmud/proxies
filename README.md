# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 404
- HTTP: 161 alive / 70 gold
- HTTPS: 53 alive / 13 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 196 alive / 165 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33305
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
