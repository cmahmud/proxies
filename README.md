# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 351
- HTTP: 127 alive / 40 gold
- HTTPS: 101 alive / 9 gold
- SOCKS4: 191 alive / 155 gold
- SOCKS5: 225 alive / 147 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32878
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
