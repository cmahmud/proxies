# SyndProxy validated proxy pool

## Current pool

- Alive now: 600
- Gold now: 414
- HTTP: 104 alive / 65 gold
- HTTPS: 134 alive / 22 gold
- SOCKS4: 179 alive / 159 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41303
- Ever gold: 1324

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
