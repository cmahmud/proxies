# SyndProxy private pool

## Current pool

- Alive now: 1100
- Gold now: 424
- HTTP: 346 alive / 86 gold
- HTTPS: 237 alive / 26 gold
- SOCKS4: 233 alive / 142 gold
- SOCKS5: 284 alive / 170 gold

## Historical pool

- Discovered: 164944
- Ever alive: 32214
- Ever gold: 1174

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
