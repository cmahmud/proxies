# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 420
- HTTP: 320 alive / 89 gold
- HTTPS: 195 alive / 31 gold
- SOCKS4: 250 alive / 145 gold
- SOCKS5: 269 alive / 155 gold

## Historical pool

- Discovered: 164927
- Ever alive: 32167
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
