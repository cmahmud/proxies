# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 411
- HTTP: 96 alive / 66 gold
- HTTPS: 182 alive / 18 gold
- SOCKS4: 179 alive / 159 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40697
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
