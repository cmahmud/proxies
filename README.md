# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 419
- HTTP: 107 alive / 73 gold
- HTTPS: 150 alive / 19 gold
- SOCKS4: 183 alive / 161 gold
- SOCKS5: 177 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40959
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
