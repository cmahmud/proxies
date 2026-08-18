# SyndProxy private pool

## Current pool

- Alive now: 981
- Gold now: 282
- HTTP: 303 alive / 27 gold
- HTTPS: 202 alive / 4 gold
- SOCKS4: 226 alive / 135 gold
- SOCKS5: 250 alive / 116 gold

## Historical pool

- Discovered: 102805
- Ever alive: 12744
- Ever gold: 399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
