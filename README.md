# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 417
- HTTP: 122 alive / 70 gold
- HTTPS: 111 alive / 20 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 191 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35248
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
