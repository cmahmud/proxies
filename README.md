# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 386
- HTTP: 125 alive / 71 gold
- HTTPS: 169 alive / 18 gold
- SOCKS4: 159 alive / 146 gold
- SOCKS5: 178 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39890
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
