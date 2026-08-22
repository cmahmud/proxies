# SyndProxy private pool

## Current pool

- Alive now: 750
- Gold now: 390
- HTTP: 186 alive / 80 gold
- HTTPS: 147 alive / 27 gold
- SOCKS4: 203 alive / 144 gold
- SOCKS5: 214 alive / 139 gold

## Historical pool

- Discovered: 163333
- Ever alive: 31885
- Ever gold: 1168

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
