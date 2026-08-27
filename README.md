# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 406
- HTTP: 89 alive / 59 gold
- HTTPS: 80 alive / 14 gold
- SOCKS4: 179 alive / 166 gold
- SOCKS5: 192 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41552
- Ever gold: 1337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
