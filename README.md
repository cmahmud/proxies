# SyndProxy private pool

## Current pool

- Alive now: 789
- Gold now: 400
- HTTP: 171 alive / 90 gold
- HTTPS: 152 alive / 20 gold
- SOCKS4: 232 alive / 145 gold
- SOCKS5: 234 alive / 145 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25207
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
