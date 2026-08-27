# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 395
- HTTP: 93 alive / 54 gold
- HTTPS: 42 alive / 14 gold
- SOCKS4: 183 alive / 163 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41656
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
