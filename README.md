# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 391
- HTTP: 132 alive / 70 gold
- HTTPS: 171 alive / 24 gold
- SOCKS4: 163 alive / 146 gold
- SOCKS5: 180 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39818
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
