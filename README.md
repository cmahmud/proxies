# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 420
- HTTP: 89 alive / 64 gold
- HTTPS: 86 alive / 22 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 192 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36090
- Ever gold: 1267

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
