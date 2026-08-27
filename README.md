# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 399
- HTTP: 107 alive / 60 gold
- HTTPS: 169 alive / 12 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 178 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40900
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
