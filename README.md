# SyndProxy private pool

## Current pool

- Alive now: 1324
- Gold now: 416
- HTTP: 483 alive / 83 gold
- HTTPS: 303 alive / 17 gold
- SOCKS4: 239 alive / 157 gold
- SOCKS5: 299 alive / 159 gold

## Historical pool

- Discovered: 134522
- Ever alive: 21899
- Ever gold: 888

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
