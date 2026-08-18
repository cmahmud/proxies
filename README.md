# SyndProxy private pool

## Current pool

- Alive now: 619
- Gold now: 250
- HTTP: 142 alive / 30 gold
- HTTPS: 88 alive / 10 gold
- SOCKS4: 204 alive / 120 gold
- SOCKS5: 185 alive / 90 gold

## Historical pool

- Discovered: 86739
- Ever alive: 6883
- Ever gold: 334

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
