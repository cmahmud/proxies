# SyndProxy validated proxy pool

## Current pool

- Alive now: 440
- Gold now: 348
- HTTP: 86 alive / 45 gold
- HTTPS: 45 alive / 12 gold
- SOCKS4: 155 alive / 147 gold
- SOCKS5: 154 alive / 144 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43640
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
