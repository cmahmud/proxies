# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 416
- HTTP: 120 alive / 71 gold
- HTTPS: 171 alive / 17 gold
- SOCKS4: 184 alive / 163 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41209
- Ever gold: 1318

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
