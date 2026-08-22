# SyndProxy private pool

## Current pool

- Alive now: 940
- Gold now: 419
- HTTP: 287 alive / 85 gold
- HTTPS: 213 alive / 28 gold
- SOCKS4: 190 alive / 134 gold
- SOCKS5: 250 alive / 172 gold

## Historical pool

- Discovered: 161925
- Ever alive: 31189
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
