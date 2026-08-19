# SyndProxy private pool

## Current pool

- Alive now: 1065
- Gold now: 513
- HTTP: 402 alive / 181 gold
- HTTPS: 296 alive / 116 gold
- SOCKS4: 186 alive / 106 gold
- SOCKS5: 181 alive / 110 gold

## Historical pool

- Discovered: 124841
- Ever alive: 19320
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
