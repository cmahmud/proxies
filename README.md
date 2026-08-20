# SyndProxy private pool

## Current pool

- Alive now: 747
- Gold now: 391
- HTTP: 175 alive / 77 gold
- HTTPS: 137 alive / 23 gold
- SOCKS4: 199 alive / 128 gold
- SOCKS5: 236 alive / 163 gold

## Historical pool

- Discovered: 150917
- Ever alive: 27084
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
