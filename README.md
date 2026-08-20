# SyndProxy private pool

## Current pool

- Alive now: 859
- Gold now: 409
- HTTP: 238 alive / 79 gold
- HTTPS: 193 alive / 22 gold
- SOCKS4: 208 alive / 149 gold
- SOCKS5: 220 alive / 159 gold

## Historical pool

- Discovered: 151050
- Ever alive: 27155
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
