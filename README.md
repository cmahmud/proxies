# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 219
- HTTP: 138 alive / 35 gold
- HTTPS: 73 alive / 6 gold
- SOCKS4: 168 alive / 88 gold
- SOCKS5: 182 alive / 90 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32783
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
