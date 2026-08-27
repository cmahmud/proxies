# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 417
- HTTP: 97 alive / 73 gold
- HTTPS: 112 alive / 23 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 176 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41825
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
