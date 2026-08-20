# SyndProxy private pool

## Current pool

- Alive now: 1535
- Gold now: 650
- HTTP: 591 alive / 218 gold
- HTTPS: 473 alive / 108 gold
- SOCKS4: 229 alive / 154 gold
- SOCKS5: 242 alive / 170 gold

## Historical pool

- Discovered: 141227
- Ever alive: 23980
- Ever gold: 967

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
