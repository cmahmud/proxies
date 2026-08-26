# SyndProxy validated proxy pool

## Current pool

- Alive now: 658
- Gold now: 386
- HTTP: 140 alive / 69 gold
- HTTPS: 175 alive / 19 gold
- SOCKS4: 163 alive / 147 gold
- SOCKS5: 180 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39747
- Ever gold: 1302

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
