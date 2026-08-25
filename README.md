# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 419
- HTTP: 95 alive / 66 gold
- HTTPS: 82 alive / 21 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 186 alive / 172 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35625
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
