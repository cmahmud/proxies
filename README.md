# SyndProxy private pool

## Current pool

- Alive now: 1298
- Gold now: 430
- HTTP: 445 alive / 94 gold
- HTTPS: 298 alive / 25 gold
- SOCKS4: 244 alive / 148 gold
- SOCKS5: 311 alive / 163 gold

## Historical pool

- Discovered: 136220
- Ever alive: 22450
- Ever gold: 900

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
