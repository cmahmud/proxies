# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 407
- HTTP: 108 alive / 66 gold
- HTTPS: 176 alive / 14 gold
- SOCKS4: 181 alive / 160 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40914
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
