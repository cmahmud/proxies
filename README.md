# SyndProxy private pool

## Current pool

- Alive now: 1811
- Gold now: 650
- HTTP: 667 alive / 226 gold
- HTTPS: 598 alive / 120 gold
- SOCKS4: 234 alive / 147 gold
- SOCKS5: 312 alive / 157 gold

## Historical pool

- Discovered: 142697
- Ever alive: 24305
- Ever gold: 982

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
