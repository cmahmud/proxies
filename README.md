# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 410
- HTTP: 98 alive / 63 gold
- HTTPS: 177 alive / 18 gold
- SOCKS4: 180 alive / 158 gold
- SOCKS5: 199 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40668
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
