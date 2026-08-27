# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 407
- HTTP: 116 alive / 65 gold
- HTTPS: 157 alive / 17 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40869
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
