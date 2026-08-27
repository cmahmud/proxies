# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 401
- HTTP: 109 alive / 66 gold
- HTTPS: 164 alive / 13 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40955
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
