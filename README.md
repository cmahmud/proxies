# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 412
- HTTP: 97 alive / 72 gold
- HTTPS: 95 alive / 19 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 179 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42020
- Ever gold: 1348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
