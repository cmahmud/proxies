# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 403
- HTTP: 107 alive / 64 gold
- HTTPS: 164 alive / 12 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40938
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
