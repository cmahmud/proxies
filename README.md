# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 410
- HTTP: 107 alive / 66 gold
- HTTPS: 166 alive / 19 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40877
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
