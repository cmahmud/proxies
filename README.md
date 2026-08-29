# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 440
- HTTP: 133 alive / 88 gold
- HTTPS: 52 alive / 25 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43664
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
