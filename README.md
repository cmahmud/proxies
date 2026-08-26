# SyndProxy validated proxy pool

## Current pool

- Alive now: 657
- Gold now: 414
- HTTP: 133 alive / 73 gold
- HTTPS: 175 alive / 23 gold
- SOCKS4: 167 alive / 156 gold
- SOCKS5: 182 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40449
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
