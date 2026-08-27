# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 417
- HTTP: 109 alive / 79 gold
- HTTPS: 117 alive / 18 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 181 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42076
- Ever gold: 1349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
