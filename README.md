# SyndProxy private pool

## Current pool

- Alive now: 1461
- Gold now: 599
- HTTP: 556 alive / 208 gold
- HTTPS: 435 alive / 105 gold
- SOCKS4: 241 alive / 149 gold
- SOCKS5: 229 alive / 137 gold

## Historical pool

- Discovered: 140469
- Ever alive: 23741
- Ever gold: 956

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
