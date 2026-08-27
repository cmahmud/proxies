# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 402
- HTTP: 74 alive / 52 gold
- HTTPS: 57 alive / 17 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41677
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
