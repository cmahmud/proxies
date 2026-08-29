# SyndProxy validated proxy pool

## Current pool

- Alive now: 446
- Gold now: 365
- HTTP: 65 alive / 48 gold
- HTTPS: 49 alive / 12 gold
- SOCKS4: 163 alive / 158 gold
- SOCKS5: 169 alive / 147 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43524
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
