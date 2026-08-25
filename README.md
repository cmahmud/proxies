# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 414
- HTTP: 94 alive / 64 gold
- HTTPS: 87 alive / 22 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35469
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
