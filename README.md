# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 411
- HTTP: 117 alive / 61 gold
- HTTPS: 146 alive / 19 gold
- SOCKS4: 180 alive / 164 gold
- SOCKS5: 181 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41269
- Ever gold: 1320

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
