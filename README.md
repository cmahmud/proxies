# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 406
- HTTP: 111 alive / 65 gold
- HTTPS: 167 alive / 14 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40937
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
