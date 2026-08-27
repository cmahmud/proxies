# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 395
- HTTP: 91 alive / 51 gold
- HTTPS: 66 alive / 17 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 186 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41611
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
