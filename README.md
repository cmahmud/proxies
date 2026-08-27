# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 417
- HTTP: 96 alive / 73 gold
- HTTPS: 110 alive / 23 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 178 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41825
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
