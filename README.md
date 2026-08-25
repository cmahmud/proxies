# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 407
- HTTP: 106 alive / 64 gold
- HTTPS: 93 alive / 20 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35441
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
