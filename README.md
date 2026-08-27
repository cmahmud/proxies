# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 417
- HTTP: 114 alive / 68 gold
- HTTPS: 168 alive / 20 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40968
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
