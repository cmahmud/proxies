# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 417
- HTTP: 100 alive / 65 gold
- HTTPS: 73 alive / 22 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 181 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35493
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
