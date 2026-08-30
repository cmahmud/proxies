# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 451
- HTTP: 121 alive / 88 gold
- HTTPS: 49 alive / 31 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 181 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43678
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
