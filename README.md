# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 411
- HTTP: 106 alive / 66 gold
- HTTPS: 162 alive / 18 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 181 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40881
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
