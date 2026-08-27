# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 412
- HTTP: 96 alive / 74 gold
- HTTPS: 106 alive / 18 gold
- SOCKS4: 179 alive / 157 gold
- SOCKS5: 178 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42029
- Ever gold: 1348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
