# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 414
- HTTP: 87 alive / 68 gold
- HTTPS: 112 alive / 21 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42589
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
