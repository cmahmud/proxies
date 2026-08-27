# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 407
- HTTP: 107 alive / 64 gold
- HTTPS: 162 alive / 13 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41215
- Ever gold: 1318

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
