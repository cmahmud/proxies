# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 395
- HTTP: 107 alive / 66 gold
- HTTPS: 48 alive / 13 gold
- SOCKS4: 171 alive / 155 gold
- SOCKS5: 187 alive / 161 gold

## Historical pool

- Discovered: 175438
- Ever alive: 33159
- Ever gold: 1228

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
