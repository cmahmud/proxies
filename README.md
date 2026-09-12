# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 469
- HTTP: 131 alive / 95 gold
- HTTPS: 57 alive / 34 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 188 alive / 177 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49395
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
