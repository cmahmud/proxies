# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 416
- HTTP: 93 alive / 64 gold
- HTTPS: 85 alive / 21 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 184 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35627
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
