# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 410
- HTTP: 111 alive / 63 gold
- HTTPS: 140 alive / 17 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41242
- Ever gold: 1319

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
