# SyndProxy validated proxy pool

## Current pool

- Alive now: 593
- Gold now: 412
- HTTP: 114 alive / 66 gold
- HTTPS: 106 alive / 18 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 192 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39310
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
