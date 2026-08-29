# SyndProxy validated proxy pool

## Current pool

- Alive now: 392
- Gold now: 339
- HTTP: 64 alive / 40 gold
- HTTPS: 26 alive / 8 gold
- SOCKS4: 152 alive / 146 gold
- SOCKS5: 150 alive / 145 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43635
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
