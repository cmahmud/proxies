# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 437
- HTTP: 134 alive / 86 gold
- HTTPS: 52 alive / 24 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43665
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
