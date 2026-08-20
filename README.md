# SyndProxy private pool

## Current pool

- Alive now: 1579
- Gold now: 612
- HTTP: 547 alive / 212 gold
- HTTPS: 451 alive / 114 gold
- SOCKS4: 227 alive / 149 gold
- SOCKS5: 354 alive / 137 gold

## Historical pool

- Discovered: 140466
- Ever alive: 23698
- Ever gold: 956

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
