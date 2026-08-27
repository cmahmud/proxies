# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 410
- HTTP: 108 alive / 64 gold
- HTTPS: 160 alive / 17 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 197 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41110
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
