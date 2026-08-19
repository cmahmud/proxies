# SyndProxy private pool

## Current pool

- Alive now: 1010
- Gold now: 340
- HTTP: 321 alive / 60 gold
- HTTPS: 255 alive / 16 gold
- SOCKS4: 228 alive / 144 gold
- SOCKS5: 206 alive / 120 gold

## Historical pool

- Discovered: 109959
- Ever alive: 15384
- Ever gold: 496

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
