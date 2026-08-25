# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 420
- HTTP: 96 alive / 64 gold
- HTTPS: 86 alive / 23 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 184 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35583
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
