# SyndProxy private pool

## Current pool

- Alive now: 1185
- Gold now: 498
- HTTP: 417 alive / 146 gold
- HTTPS: 283 alive / 91 gold
- SOCKS4: 230 alive / 124 gold
- SOCKS5: 255 alive / 137 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17282
- Ever gold: 661

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
