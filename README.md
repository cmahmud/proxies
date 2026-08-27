# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 407
- HTTP: 111 alive / 66 gold
- HTTPS: 172 alive / 15 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 191 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41083
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
