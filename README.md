# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 384
- HTTP: 113 alive / 55 gold
- HTTPS: 49 alive / 10 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33440
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
