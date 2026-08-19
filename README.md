# SyndProxy private pool

## Current pool

- Alive now: 1154
- Gold now: 533
- HTTP: 428 alive / 157 gold
- HTTPS: 297 alive / 106 gold
- SOCKS4: 225 alive / 142 gold
- SOCKS5: 204 alive / 128 gold

## Historical pool

- Discovered: 127372
- Ever alive: 19931
- Ever gold: 804

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
