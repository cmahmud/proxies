# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 412
- HTTP: 93 alive / 61 gold
- HTTPS: 80 alive / 20 gold
- SOCKS4: 179 alive / 165 gold
- SOCKS5: 191 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41544
- Ever gold: 1337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
