# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 411
- HTTP: 138 alive / 72 gold
- HTTPS: 150 alive / 22 gold
- SOCKS4: 174 alive / 153 gold
- SOCKS5: 183 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40369
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
