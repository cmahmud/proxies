# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 393
- HTTP: 136 alive / 75 gold
- HTTPS: 180 alive / 22 gold
- SOCKS4: 163 alive / 145 gold
- SOCKS5: 169 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39935
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
