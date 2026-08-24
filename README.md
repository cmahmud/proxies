# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 406
- HTTP: 112 alive / 69 gold
- HTTPS: 49 alive / 15 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 181 alive / 163 gold

## Historical pool

- Discovered: 177314
- Ever alive: 33276
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
