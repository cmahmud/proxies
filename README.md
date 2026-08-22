# SyndProxy private pool

## Current pool

- Alive now: 789
- Gold now: 343
- HTTP: 234 alive / 85 gold
- HTTPS: 163 alive / 22 gold
- SOCKS4: 182 alive / 112 gold
- SOCKS5: 210 alive / 124 gold

## Historical pool

- Discovered: 167410
- Ever alive: 32579
- Ever gold: 1190

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
