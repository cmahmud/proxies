# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 405
- HTTP: 92 alive / 56 gold
- HTTPS: 109 alive / 19 gold
- SOCKS4: 178 alive / 167 gold
- SOCKS5: 194 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41515
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
