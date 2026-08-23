# SyndProxy validated proxy pool

## Current pool

- Alive now: 789
- Gold now: 197
- HTTP: 321 alive / 36 gold
- HTTPS: 54 alive / 5 gold
- SOCKS4: 211 alive / 68 gold
- SOCKS5: 203 alive / 88 gold

## Historical pool

- Discovered: 170566
- Ever alive: 32774
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
