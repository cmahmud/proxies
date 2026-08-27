# SyndProxy validated proxy pool

## Current pool

- Alive now: 656
- Gold now: 405
- HTTP: 122 alive / 60 gold
- HTTPS: 171 alive / 11 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 186 alive / 174 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40812
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
