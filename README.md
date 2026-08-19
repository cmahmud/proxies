# SyndProxy private pool

## Current pool

- Alive now: 1167
- Gold now: 606
- HTTP: 450 alive / 190 gold
- HTTPS: 265 alive / 112 gold
- SOCKS4: 229 alive / 146 gold
- SOCKS5: 223 alive / 158 gold

## Historical pool

- Discovered: 124855
- Ever alive: 19426
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
