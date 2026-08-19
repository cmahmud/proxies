# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 556
- HTTP: 365 alive / 170 gold
- HTTPS: 228 alive / 92 gold
- SOCKS4: 231 alive / 147 gold
- SOCKS5: 210 alive / 147 gold

## Historical pool

- Discovered: 124833
- Ever alive: 19171
- Ever gold: 731

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
