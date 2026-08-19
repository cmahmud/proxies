# SyndProxy private pool

## Current pool

- Alive now: 1040
- Gold now: 394
- HTTP: 323 alive / 77 gold
- HTTPS: 228 alive / 15 gold
- SOCKS4: 257 alive / 148 gold
- SOCKS5: 232 alive / 154 gold

## Historical pool

- Discovered: 131098
- Ever alive: 20522
- Ever gold: 868

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
