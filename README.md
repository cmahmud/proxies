# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 348
- HTTP: 122 alive / 38 gold
- HTTPS: 118 alive / 9 gold
- SOCKS4: 183 alive / 153 gold
- SOCKS5: 221 alive / 148 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32878
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
