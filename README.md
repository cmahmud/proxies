# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 443
- HTTP: 105 alive / 81 gold
- HTTPS: 42 alive / 28 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 177 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43686
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
