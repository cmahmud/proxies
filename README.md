# SyndProxy validated proxy pool

## Current pool

- Alive now: 443
- Gold now: 354
- HTTP: 87 alive / 46 gold
- HTTPS: 50 alive / 16 gold
- SOCKS4: 151 alive / 148 gold
- SOCKS5: 155 alive / 144 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43642
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
