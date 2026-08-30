# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 451
- HTTP: 128 alive / 87 gold
- HTTPS: 53 alive / 32 gold
- SOCKS4: 164 alive / 162 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43678
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
