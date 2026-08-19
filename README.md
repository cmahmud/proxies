# SyndProxy private pool

## Current pool

- Alive now: 1049
- Gold now: 458
- HTTP: 332 alive / 120 gold
- HTTPS: 242 alive / 72 gold
- SOCKS4: 237 alive / 137 gold
- SOCKS5: 238 alive / 129 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16782
- Ever gold: 623

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
