# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 409
- HTTP: 98 alive / 57 gold
- HTTPS: 66 alive / 19 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 197 alive / 171 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36215
- Ever gold: 1269

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
