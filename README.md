# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 196
- HTTP: 169 alive / 42 gold
- HTTPS: 41 alive / 8 gold
- SOCKS4: 138 alive / 64 gold
- SOCKS5: 159 alive / 82 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32727
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
