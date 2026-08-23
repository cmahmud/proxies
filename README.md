# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 342
- HTTP: 128 alive / 35 gold
- HTTPS: 122 alive / 8 gold
- SOCKS4: 181 alive / 153 gold
- SOCKS5: 214 alive / 146 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32878
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
