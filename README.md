# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 414
- HTTP: 94 alive / 69 gold
- HTTPS: 80 alive / 20 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 176 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41755
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
