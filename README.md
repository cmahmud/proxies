# SyndProxy private pool

## Current pool

- Alive now: 1202
- Gold now: 498
- HTTP: 439 alive / 148 gold
- HTTPS: 282 alive / 90 gold
- SOCKS4: 228 alive / 123 gold
- SOCKS5: 253 alive / 137 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17282
- Ever gold: 661

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
