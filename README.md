# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 447
- HTTP: 106 alive / 82 gold
- HTTPS: 43 alive / 31 gold
- SOCKS4: 164 alive / 163 gold
- SOCKS5: 177 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43684
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
