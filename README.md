# SyndProxy private pool

## Current pool

- Alive now: 915
- Gold now: 391
- HTTP: 268 alive / 88 gold
- HTTPS: 189 alive / 25 gold
- SOCKS4: 225 alive / 141 gold
- SOCKS5: 233 alive / 137 gold

## Historical pool

- Discovered: 155800
- Ever alive: 29372
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
