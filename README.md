# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 403
- HTTP: 118 alive / 63 gold
- HTTPS: 158 alive / 15 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40868
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
