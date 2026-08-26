# SyndProxy validated proxy pool

## Current pool

- Alive now: 673
- Gold now: 407
- HTTP: 144 alive / 81 gold
- HTTPS: 194 alive / 25 gold
- SOCKS4: 162 alive / 146 gold
- SOCKS5: 173 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39975
- Ever gold: 1305

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
