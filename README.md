# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 373
- HTTP: 229 alive / 88 gold
- HTTPS: 41 alive / 31 gold
- SOCKS4: 102 alive / 76 gold
- SOCKS5: 207 alive / 178 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48621
- Ever gold: 1561

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
