# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 413
- HTTP: 96 alive / 73 gold
- HTTPS: 121 alive / 22 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 175 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41826
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
