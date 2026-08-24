# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 383
- HTTP: 102 alive / 62 gold
- HTTPS: 47 alive / 14 gold
- SOCKS4: 163 alive / 152 gold
- SOCKS5: 170 alive / 155 gold

## Historical pool

- Discovered: 176375
- Ever alive: 33205
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
