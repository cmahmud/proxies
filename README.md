# SyndProxy private pool

## Current pool

- Alive now: 988
- Gold now: 340
- HTTP: 304 alive / 60 gold
- HTTPS: 248 alive / 16 gold
- SOCKS4: 228 alive / 144 gold
- SOCKS5: 208 alive / 120 gold

## Historical pool

- Discovered: 109959
- Ever alive: 15384
- Ever gold: 496

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
