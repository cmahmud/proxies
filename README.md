# SyndProxy validated proxy pool

## Current pool

- Alive now: 656
- Gold now: 414
- HTTP: 153 alive / 76 gold
- HTTPS: 155 alive / 24 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 183 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40339
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
