# SyndProxy private pool

## Current pool

- Alive now: 991
- Gold now: 367
- HTTP: 298 alive / 79 gold
- HTTPS: 240 alive / 22 gold
- SOCKS4: 217 alive / 123 gold
- SOCKS5: 236 alive / 143 gold

## Historical pool

- Discovered: 165816
- Ever alive: 32324
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
