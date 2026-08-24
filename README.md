# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 393
- HTTP: 104 alive / 57 gold
- HTTPS: 64 alive / 15 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 175 alive / 162 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33501
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
