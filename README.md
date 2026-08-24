# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 386
- HTTP: 112 alive / 64 gold
- HTTPS: 46 alive / 15 gold
- SOCKS4: 167 alive / 152 gold
- SOCKS5: 171 alive / 155 gold

## Historical pool

- Discovered: 176375
- Ever alive: 33205
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
