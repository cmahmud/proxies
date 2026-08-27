# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 412
- HTTP: 90 alive / 74 gold
- HTTPS: 102 alive / 17 gold
- SOCKS4: 179 alive / 158 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42026
- Ever gold: 1348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
