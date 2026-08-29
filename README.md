# SyndProxy validated proxy pool

## Current pool

- Alive now: 371
- Gold now: 321
- HTTP: 52 alive / 32 gold
- HTTPS: 17 alive / 1 gold
- SOCKS4: 147 alive / 144 gold
- SOCKS5: 155 alive / 144 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43632
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
