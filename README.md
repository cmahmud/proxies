# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 419
- HTTP: 102 alive / 64 gold
- HTTPS: 88 alive / 24 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 189 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35648
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
