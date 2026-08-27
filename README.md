# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 411
- HTTP: 115 alive / 68 gold
- HTTPS: 172 alive / 15 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40923
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
