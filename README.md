# SyndProxy private pool

## Current pool

- Alive now: 936
- Gold now: 441
- HTTP: 275 alive / 100 gold
- HTTPS: 173 alive / 32 gold
- SOCKS4: 220 alive / 145 gold
- SOCKS5: 268 alive / 164 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31046
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
