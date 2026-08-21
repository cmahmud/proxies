# SyndProxy private pool

## Current pool

- Alive now: 894
- Gold now: 397
- HTTP: 238 alive / 77 gold
- HTTPS: 175 alive / 22 gold
- SOCKS4: 253 alive / 159 gold
- SOCKS5: 228 alive / 139 gold

## Historical pool

- Discovered: 156830
- Ever alive: 29622
- Ever gold: 1133

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
