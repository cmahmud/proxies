# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 443
- HTTP: 130 alive / 89 gold
- HTTPS: 60 alive / 27 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 180 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43663
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
