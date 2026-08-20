# SyndProxy private pool

## Current pool

- Alive now: 768
- Gold now: 394
- HTTP: 182 alive / 73 gold
- HTTPS: 146 alive / 18 gold
- SOCKS4: 219 alive / 150 gold
- SOCKS5: 221 alive / 153 gold

## Historical pool

- Discovered: 151061
- Ever alive: 27365
- Ever gold: 1095

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
