# SyndProxy validated proxy pool

## Current pool

- Alive now: 416
- Gold now: 333
- HTTP: 54 alive / 39 gold
- HTTPS: 32 alive / 7 gold
- SOCKS4: 163 alive / 133 gold
- SOCKS5: 167 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43550
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
