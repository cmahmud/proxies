# SyndProxy private pool

## Current pool

- Alive now: 1033
- Gold now: 325
- HTTP: 365 alive / 36 gold
- HTTPS: 204 alive / 10 gold
- SOCKS4: 239 alive / 147 gold
- SOCKS5: 225 alive / 132 gold

## Historical pool

- Discovered: 106888
- Ever alive: 14127
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
