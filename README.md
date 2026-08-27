# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 412
- HTTP: 106 alive / 65 gold
- HTTPS: 162 alive / 18 gold
- SOCKS4: 183 alive / 157 gold
- SOCKS5: 198 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40674
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
